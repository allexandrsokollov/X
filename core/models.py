import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=False)
    updated_at = models.DateTimeField(auto_now=True, db_index=False)


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=128, unique=True, db_index=True)


class Project(BaseModel):
    title = models.CharField(max_length=512)
    description = models.TextField()
    managers = models.ManyToManyField(User, related_name="project_managers")
    participants = models.ManyToManyField(User, related_name="projects_participants")
    progress = models.FloatField(default=0)


class Feature(BaseModel):
    title = models.CharField(max_length=512)
    description = models.TextField()
    project = models.ForeignKey(
        Project, null=True, on_delete=models.SET_NULL, related_name="features"
    )
    executors = models.ManyToManyField(
        User, related_name="feature_executors", default=[]
    )


class Task(BaseModel):
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="task_owner"
    )
    feature = models.ForeignKey(
        Feature, on_delete=models.SET_NULL, null=True, related_name="tasks"
    )
    title = models.CharField(max_length=512)
    is_completed = models.BooleanField(default=False)
    description = models.TextField()
