from django.db import transaction

from core.models import Task, User, Feature
from core.repositories.abstract_repos import CRUDRepo
from core.repositories.feature_repository import FeatureRepo
from core.repositories.task_repository import TaskRepo


class TaskService:
    def __init__(self):
        self.feature_repo = FeatureRepo(Feature)
        self.user_repo = CRUDRepo(User)
        self.task_repo = TaskRepo()

    @transaction.atomic
    def save(self, **kwargs):
        owner = None
        feature = None

        if "owner" in kwargs:
            owner = self.user_repo.get(pk=kwargs["owner"])
            del kwargs["owner"]

        if "feature" in kwargs:
            feature = self.feature_repo.get(pk=kwargs["feature"])
            del kwargs["feature"]

        new_task = self.task_repo.create(**kwargs)
        new_task.owner = owner
        new_task.feature = feature

        new_task.save()

        return new_task

    @transaction.atomic
    def update(self, pk, **kwargs):
        owner = None
        feature = None

        if "owner" in kwargs:
            owner = self.user_repo.get(pk=kwargs["owner"])
            del kwargs["owner"]

        if "feature" in kwargs:
            feature = self.feature_repo.get(pk=kwargs["feature"])
            del kwargs["feature"]

        self.task_repo.update(
            **kwargs,
            pk=pk,
            owner=owner,
            feature=feature,
        )
