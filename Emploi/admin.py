from django.contrib import admin

from Emploi.models import Emploi
from Etudiants.models import Etudiant



#admin.site.register(Emploi)



@admin.register(Emploi)
class EmploiAdmin(admin.ModelAdmin):
    list_display=('etudiant','entreprise','poste','typecont')
    list_filter=('etudiant','entreprise','poste','typecont')
    search_fields=('typecont','entreprise')
