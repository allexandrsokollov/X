from copy import copy, deepcopy
from typing import override

from django.db import transaction

from core.repositories.abstract_repos import CRUDRepo


class FeatureRepo(CRUDRepo):
    @override
    def get(self, pk):
        feature = (
            self.model.objects.filter(id=pk)
            .select_related("project")
            .prefetch_related("executors")
            .first()
        )
        return feature

    @override
    @transaction.atomic
    def create(self, **kwargs):
        executors = copy(kwargs["executors"])
        del kwargs["executors"]

        feature = self.model.objects.create(**kwargs)
        feature.executors.set(executors)
        feature.save()

        return feature

    @override
    @transaction.atomic
    def update(self, pk, **kwargs):
        feature = self.get(pk)

        executors = deepcopy(kwargs["executors"])
        del kwargs["executors"]

        for attribute, value in kwargs.items():
            feature.__setattr__(attribute, value)

        feature.executors.set(executors)
        feature.save()

        kwargs["executors"] = executors

        return feature
