from django.urls import path, include
from . import views

urlpatterns = [
    path("customer/signup/", views.CustomerSignup.as_view()),
    path("customer/login/", views.CustomerLogin.as_view()),
    path("getProfile/<username>/", views.GetProfile.as_view()),
]
