from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("createTransaction/", views.createTransaction, name="createTransaction"),
    path("",  views.home, name='home'),
]











