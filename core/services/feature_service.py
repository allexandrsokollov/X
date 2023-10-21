from copy import copy

from django.db import transaction

from core.models import Feature, Project
from core.repositories.feature_repository import FeatureRepo
from core.repositories.project_repository import ProjectRepo


class FeatureService:
    def __init__(self):
        self.feature_repo = FeatureRepo(Feature)
        self.project_repo = ProjectRepo(Project)

    @transaction.atomic
    def create(self, **kwargs):
        project = copy(kwargs['project'])
        del kwargs['project']

        feature = self.feature_repo.create(**kwargs)

        project = self.project_repo.get(pk=project)
        feature.project = project
        feature.save()

        return feature

    @transaction.atomic
    def update(self, pk,  **kwargs):
        if 'project' in kwargs:
            project = kwargs['project']
            del kwargs['project']

            project_instance = self.project_repo.get(pk=project)
            updated_feature = self.feature_repo.update(pk, **kwargs)
            updated_feature.project = project_instance
            updated_feature.save()
        else:
            updated_feature = self.feature_repo.update(pk, **kwargs)

        return updated_feature
