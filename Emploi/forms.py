from django import forms
from .models import Emploi







class EmploiForm(forms.ModelForm):
    
    #check = forms.BooleanField()
    
    class Meta:
        model = Emploi
        fields =['entreprise','typecont','poste','mois_date_debut','annee_date_debut','mois_date_fin','annee_date_fin','description']
    
    
    
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  if not self.fields['check'].initial:
       #     self.fields['moisdatefin'].disabled = True
        #    self.fields['anneedatefin'].disabled = True