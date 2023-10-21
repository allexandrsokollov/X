from django.urls import path

from core.controllers.feature_api import (
    FeatureGetAllCreateApiView,
    FeatureGetDeleteUpdateApiView,
)
from core.controllers.project_api import (
    ProjectGetAllCreateApiView,
    ProjectGetDeleteUpdateApiView,
)
from core.controllers.task_api import (
    TaskGetAllCreateApiView,
    TaskGetDeleteUpdateApiView,
)
from core.controllers.user_api import (
    UserGetAllCreateApiView,
    UserGetDeleteUpdateApiView,
)

urlpatterns = [
    path("user/", UserGetAllCreateApiView.as_view()),
    path("user/<str:pk>", UserGetDeleteUpdateApiView.as_view()),
    path("projects/", ProjectGetAllCreateApiView.as_view()),
    path("projects/<str:pk>", ProjectGetDeleteUpdateApiView.as_view()),
    path("features/", FeatureGetAllCreateApiView.as_view()),
    path("features/<str:pk>", FeatureGetDeleteUpdateApiView.as_view()),
    path("task/", TaskGetAllCreateApiView.as_view()),
    path("task/<str:pk>", TaskGetDeleteUpdateApiView.as_view()),
]
