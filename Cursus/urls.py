from django.urls import path

from Cursus import views

urlpatterns = [
    path("<int:user_id>/", views.cursus_home, name="cursus"),
]