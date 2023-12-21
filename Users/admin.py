from django.contrib import admin

from Users.models import User

# Register your models here.




#admin.site.register(User)


@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display=('first_name','last_name','is_superuser','is_etudiant','is_personnel','is_admin')
    #list_filter=('email',)
    search_fields=('email',)