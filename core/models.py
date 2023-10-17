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
    managers = models.ManyToManyField(User)
    participants = models.ManyToManyField(User)
    progress = models.FloatField(default=0)


class Feature(BaseModel):
    title = models.CharField(max_length=512)
    description = models.TextField()
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    executors = models.ManyToManyField(User)


class Task(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=512)
    description = models.TextField()