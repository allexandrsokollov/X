from copy import copy
from typing import override

from django.db import transaction

from core.exceptions.repository_exceptions import NotFoundException
from core.repositories.abstract_repos import CRUDRepo


class ProjectRepo(CRUDRepo):
    @override
    @transaction.atomic
    def get(self, pk):
        project = (
            self.model.objects.filter(id=pk)
            .prefetch_related("managers", "participants")
            .first()
        )
        return project

    @override
    @transaction.atomic
    def create(self, **kwargs):
        managers = copy(kwargs["managers"])
        participants = copy(kwargs["participants"])
        del kwargs["managers"]
        del kwargs["participants"]

        created = self.model.objects.create(**kwargs)
        created.managers.set(managers)
        created.participants.set(participants)
        created.save()

        return created

    @override
    @transaction.atomic()
    def update(self, pk, **kwargs):
        managers = copy(kwargs["managers"])
        participants = copy(kwargs["participants"])
        del kwargs["managers"]
        del kwargs["participants"]

        project = self.model.objects.filter(id=pk).first()

        if not project:
            raise NotFoundException

        for attribute, value in kwargs.items():
            project.__setattr__(attribute, value)

        project.participants.set(participants)
        project.managers.set(managers)

        project.save()
        return project
