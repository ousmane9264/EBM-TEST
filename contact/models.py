from django.db import models
from django import forms
# # Create your models here.
class Contact(models.Model):

    nom = models.CharField(max_length=800, null=True)
    email = models.EmailField(max_length=500)
    telephone = models.IntegerField()
    niveau_etude = models.CharField(max_length=500,)
    centre_souhaite = models.CharField( max_length=500,)
    formation_souhaitee = models.CharField(max_length=500,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # LEVEL_CHOICES = (('BAC', 'BAC'),('LICENCE', 'LICENCE'), ('MASTER', 'MASTER'), ('DOCTORAT','DOCTORAT'))
    # niveau_etude = forms.ChoiceField(label="Quel est votre niveau d'étude *", choices=LEVEL_CHOICES,
    # widget=forms.Select(attrs={"class":"form-control"}))
    # CENTER_CHOICES = (('Casablanca', 'Casablanca'),('Montréal', 'Montréal'))
    # centre_souhaite = forms.ChoiceField(label="Centre souhaité *", choices=CENTER_CHOICES,
    # widget=forms.Select(attrs={"class":"form-control"}))
    # FORMATIONS_CHOICES = (('LOGISTIQUE ET TRANSPORT', 'LOGISTIQUE ET TRANSPORT'),('INFORMATIQUE', 'INFORMATIQUE'), ('MINE','MINE'), ('COMMERCE','COMMERCE'))
    # centre_souhaite = forms.ChoiceField(label="Centre souhaité *", choices=FORMATIONS_CHOICES,
    # widget=forms.Select(attrs={"class":"form-control"}))
