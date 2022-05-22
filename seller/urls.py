from django.urls import path
from . import views

urlpatterns = [
    path("seller_dash/",views.dash, name="dash"),
    path("logout/", views.logoutUser, name="logoutUser"),
]
