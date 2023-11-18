from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Etudiants.urls")),
    path("cursus/", include("Cursus.urls")),
    path("emploi/", include("Emploi.urls")),
    path("competence/", include("competence.urls")),
    path("personnel/", include("Personnels.urls")),
]
