from django import forms
from .models import Competence



class CompetenceForm(forms.ModelForm):
    
    class Meta:
        model = Competence
        fields =['nom','pourcentage','description']
       
        
        widgets ={"nom": forms.TextInput(attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 ',}),
                 "pourcentage": forms.NumberInput(attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',}),
                 "description": forms.Textarea(attrs={'rows':'3','placeholder':"Description du competence.",'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',}),
                }
                #'required':True,

        
 