from django.contrib import admin
from Emploi.models import Emploi
from Cursus.models import Cursus
from competence.models import Competence

from Etudiants.models import Etudiant, PhotoCouverture, PhotoProfil

# Register your models here.
#admin.site.register(Etudiant) on peux faire ça


#@admin.register(Etudiant,AUTRE MODEL)  # SI J'AVAIS UN AUTRE MODEL JE PEUX L'AJOUTER
#class GenericAdmin(admin.ModelAdmin):
   # pass
   


class CursusAdd(admin.TabularInline):
    model=Cursus
    extra=0


class EmploiAdd(admin.TabularInline):
    model=Emploi
    extra=0
    

class CompetenceAdd(admin.TabularInline):
    model=Competence
    extra=0
    

class CouvertureAdd(admin.TabularInline):
    model=PhotoCouverture
    extra=0
    

class ProfilAdd(admin.TabularInline):
    model=PhotoProfil
    extra=0
    
    
  
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display=('code_permenant','first_name','last_name','email')
    list_filter=('code_permenant','profession','niveau_actuel')
    search_fields=('code_permenant', )
    inlines=(ProfilAdd,CouvertureAdd,CursusAdd,EmploiAdd,CompetenceAdd)


@admin.register(PhotoProfil)
class Etudiant_Photo_Profil(admin.ModelAdmin):
    list_display=('profil',)
    list_filter=('profil',)
    search_fields=('profil',)


@admin.register(PhotoCouverture)
class Etudiant_Photo_Couverture(admin.ModelAdmin):
    list_display=('couverture',)
    list_filter=('couverture',)
    search_fields=('couverture', )
    
