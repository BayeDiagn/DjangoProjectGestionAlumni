from django.urls import path

from . import views

urlpatterns = [
    path("", views.personnel_home, name="personnel_home"),
]