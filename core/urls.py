from django.urls import path

from core.controllers.user_api import UserApiView

urlpatterns = [
    path('users/', UserApiView.as_view()),
    path('users/<str:pk>/', UserApiView.as_view()),
]