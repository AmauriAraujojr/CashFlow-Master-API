from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/login/", views.LoginJWTView.as_view()),
    path("user/<int:pk>/", views.UserDetailView.as_view())
]
