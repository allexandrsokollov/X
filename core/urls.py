from django.urls import path

from core.controllers.user_api import UserGetAllCreateApiView, GetDeleteUpdateApiView

urlpatterns = [
    path('user/', UserGetAllCreateApiView.as_view()),
    path('user/<str:pk>', GetDeleteUpdateApiView.as_view()),
]
