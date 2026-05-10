from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Membre, Cotisation


class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'telephone', 'email', 'fonction', 'date_inscription', 'niveau_scolarite', 'actif']
        widgets = {
            'date_inscription': forms.DateInput(attrs={'type': 'date'}),
        }


class CotisationForm(forms.ModelForm):
    class Meta:
        model = Cotisation
        fields = ['membre', 'annee', 'montant', 'statut_paiement']


class InscriptionForm(UserCreationForm):
    nom = forms.CharField(max_length=100, label='Nom')
    prenom = forms.CharField(max_length=100, label='Prénom')
    email = forms.EmailField(label='Email')
    telephone = forms.CharField(max_length=20, required=False, label='Téléphone')

    class Meta:
        model = User
        fields = ['username', 'nom', 'prenom', 'email', 'telephone', 'password1', 'password2']
