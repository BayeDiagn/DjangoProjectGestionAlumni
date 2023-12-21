from django.contrib import admin

from Personnels.models import Personnel

# Register your models here.



@admin.register(Personnel)
class Personnel(admin.ModelAdmin):
    list_display=('first_name','last_name','filiere')
    list_filter=('filiere',)
    search_fields=('filiere',)
    

