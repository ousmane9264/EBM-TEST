from django import forms
from .models import Contact

# # Create your models here.
class Form(forms.Form):

    class Meta:
        model   = Contact
        fields = ('nom', 'email', 'telephone', 'niveau_etude', 'centre_souhaite', 'formation_souhaitee')
        widgets = {
            'nom': forms.fields.TextInput(attrs={
                'class': 'validate',
            }),
            'email': forms.fields.TextInput(attrs={
                'class': 'validate',
                'type': 'email',
            }),
            'telephone': forms.fields.TextInput(attrs={
                'class': 'validate',
                'type': 'number',
            }),
            'niveau_etude': forms.Select(attrs={
                'name': 'niveau_etude',
                'class': 'validate'
            }),
            'centre_souhaite': forms.Select(attrs={
                'name': 'centre_souhaite',
                'class': 'validate'
            }),
            'formation_souhaitee': forms.Select(attrs={
                'name': 'formation_souhaitee',
                'class': 'validate'
            }),
        }
