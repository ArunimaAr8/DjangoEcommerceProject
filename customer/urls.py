from django.urls import path, include
from .import views

urlpatterns = [
    path("customer/signup/", views.CustomerSignup.as_view())
]