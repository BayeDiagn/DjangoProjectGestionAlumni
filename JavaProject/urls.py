from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Etudiants.urls")),
    path("cursus/", include("Cursus.urls")),
    path("emploi/", include("Emploi.urls")),
    path("competence/", include("competence.urls")),
    path("personnel/", include("Personnels.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
