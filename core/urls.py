from django.urls import path

from core.controllers.user_api import UserGetAllCreateApiView, UserGetUpdateApiView

urlpatterns = [
    path('users/', UserGetAllCreateApiView.as_view()),
    path('users/<str:pk>/', UserGetUpdateApiView.as_view()),
]