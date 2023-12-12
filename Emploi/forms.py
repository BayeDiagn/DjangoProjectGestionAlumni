from django import forms
from .models import Emploi







class EmploiForm(forms.ModelForm):
    
    #check = forms.BooleanField()
    
    class Meta:
        model = Emploi
        fields =['entreprise','typecont','poste','mois_date_debut','annee_date_debut','mois_date_fin','annee_date_fin','description']
    
        widgets ={"entreprise": forms.TextInput(attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 ',}),
                 "typecont": forms.TextInput(attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',}),
                 "poste": forms.TextInput(attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',}),
                 "description": forms.Textarea(attrs={'rows':'3','placeholder':"Description du poste.",'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',}),
                }
    
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  if not self.fields['check'].initial:
       #     self.fields['moisdatefin'].disabled = True
        #    self.fields['anneedatefin'].disabled = True