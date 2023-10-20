from django.urls import path

from core.controllers.project_api import ProjectGetAllCreateApiView, ProjectGetDeleteUpdateApiView
from core.controllers.user_api import UserGetAllCreateApiView, UserGetDeleteUpdateApiView

urlpatterns = [
    path('user/', UserGetAllCreateApiView.as_view()),
    path('user/<str:pk>', UserGetDeleteUpdateApiView.as_view()),
    path('projects/', ProjectGetAllCreateApiView.as_view()),
    path('projects/<str:pk>', ProjectGetDeleteUpdateApiView.as_view()),
]
