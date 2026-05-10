from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Fonction(models.Model):
    titre_poste = models.CharField(max_length=100)
    responsabilite = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Fonction'
        verbose_name_plural = 'Fonctions'
        ordering = ['titre_poste']

    def __str__(self):
        return self.titre_poste


class Membre(models.Model):
    NIVEAU_SCOLARITE_CHOICES = [
        ('primaire', 'Primaire'),
        ('college', 'Collège'),
        ('lycee', 'Lycée'),
        ('bac', 'Baccalauréat'),
        ('licence', 'Licence'),
        ('master', 'Master'),
        ('doctorat', 'Doctorat'),
        ('autre', 'Autre'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='membre'
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    fonction = models.ForeignKey(
        Fonction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='membres'
    )
    date_inscription = models.DateField(default=timezone.now)
    niveau_scolarite = models.CharField(
        max_length=20,
        choices=NIVEAU_SCOLARITE_CHOICES,
        default='autre'
    )
    actif = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Membre'
        verbose_name_plural = 'Membres'
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    @property
    def anciennete(self):
        delta = timezone.now().date() - self.date_inscription
        annees = delta.days // 365
        mois = (delta.days % 365) // 30
        if annees > 0:
            return f"{annees} an(s) et {mois} mois"
        return f"{mois} mois"


class Cotisation(models.Model):
    STATUT_CHOICES = [
        ('paye', 'Payé'),
        ('en_attente', 'En attente'),
        ('impaye', 'Impayé'),
    ]

    membre = models.ForeignKey(
        Membre,
        on_delete=models.CASCADE,
        related_name='cotisations'
    )
    annee = models.PositiveIntegerField()
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    statut_paiement = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente'
    )

    class Meta:
        verbose_name = 'Cotisation'
        verbose_name_plural = 'Cotisations'
        ordering = ['-annee']
        unique_together = ('membre', 'annee')

    def __str__(self):
        return f"{self.membre} — {self.annee} ({self.get_statut_paiement_display()})"
