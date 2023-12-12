from django.contrib import admin
from .models import Cursus


#admin.site.register(Cursus)


@admin.register(Cursus)
class CursusAdmin(admin.ModelAdmin):
    list_display=('etudiant','etablissement','diplome_name','cycle','autre_cycle')
    list_filter=('etudiant','etablissement','diplome_name','cycle')
    search_fields=('cycle','etablissement')
