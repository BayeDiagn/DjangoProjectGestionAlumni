from django import forms
from .models import Emploi



class EmploiForm(forms.ModelForm):
    
    class Meta:
        model = Emploi
        fields =['entreprise','typecont','poste','anneedebut','anneeFin','description']
       
 