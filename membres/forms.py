from django import forms
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
