from django import forms
from .models import Cursus



class CursusForm(forms.ModelForm):
    
    class Meta:
        model = Cursus
        fields =['etablissement','diplome_name','mois_date_debut','annee_date_debut','mois_date_fin','annee_date_fin']
       
        widgets ={"etablissement": forms.TextInput(attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 ',}),
                 "diplome_name": forms.TextInput(attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',}),
                }