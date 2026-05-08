from django.contrib import admin
from .models import Fonction, Membre, Cotisation


@admin.register(Fonction)
class FonctionAdmin(admin.ModelAdmin):
    list_display = ('titre_poste', 'responsabilite')
    search_fields = ('titre_poste',)


class CotisationInline(admin.TabularInline):
    model = Cotisation
    extra = 1


@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'fonction', 'telephone', 'email', 'niveau_scolarite', 'date_inscription', 'actif')
    list_filter = ('fonction', 'niveau_scolarite', 'actif')
    search_fields = ('nom', 'prenom', 'email', 'telephone')
    inlines = [CotisationInline]
    list_per_page = 25


@admin.register(Cotisation)
class CotisationAdmin(admin.ModelAdmin):
    list_display = ('membre', 'annee', 'montant', 'statut_paiement')
    list_filter = ('statut_paiement', 'annee')
    search_fields = ('membre__nom', 'membre__prenom')
