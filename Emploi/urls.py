from django.urls import path

from . import views

urlpatterns = [
    path("", views.emploi_home,name="emploi_home"),
]