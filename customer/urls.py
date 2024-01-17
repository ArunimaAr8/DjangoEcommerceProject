from django.urls import path
from . import views

urlpatterns = [
    path("customer/signup/", views.CustomerSignup.as_view()),
    path("customer/login/", views.CustomerLogin.as_view()),
    path("getProfile/<username>/", views.GetProfile.as_view()),
    path("updateProfile/", views.UpdateProfile.as_view()),
    path("deleteCustomer/<username>/", views.DeleteCustomer.as_view()),
]
