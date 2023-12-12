from django.contrib import admin

from competence.models import Competence



#admin.site.register(Competence)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display=('etudiant','nom','pourcentage')
    list_filter=('etudiant','nom','pourcentage')
    search_fields=('nom',)