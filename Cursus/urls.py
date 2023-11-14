from django.urls import path

from Cursus import views

urlpatterns = [
    path("", views.cursus_home, name="cursus_home"),
]