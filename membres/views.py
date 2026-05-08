from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import Membre, Fonction, Cotisation
from .forms import MembreForm, CotisationForm


def annuaire(request):
    membres = Membre.objects.filter(actif=True).select_related('fonction')
    recherche = request.GET.get('q', '')
    fonction_id = request.GET.get('fonction', '')
    niveau = request.GET.get('niveau', '')

    if recherche:
        membres = membres.filter(
            Q(nom__icontains=recherche) | Q(prenom__icontains=recherche)
        )
    if fonction_id:
        membres = membres.filter(fonction_id=fonction_id)
    if niveau:
        membres = membres.filter(niveau_scolarite=niveau)

    fonctions = Fonction.objects.all()
    niveaux = Membre.NIVEAU_SCOLARITE_CHOICES

    return render(request, 'membres/annuaire.html', {
        'membres': membres,
        'fonctions': fonctions,
        'niveaux': niveaux,
        'recherche': recherche,
        'fonction_id': fonction_id,
        'niveau_selectionne': niveau,
    })


def detail_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    return render(request, 'membres/detail_membre.html', {'membre': membre})


@login_required
def liste_membres(request):
    membres = Membre.objects.all().select_related('fonction')
    return render(request, 'membres/liste_membres.html', {'membres': membres})


@login_required
def ajouter_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'membres/form_membre.html', {'form': form, 'titre': 'Ajouter un membre'})


@login_required
def modifier_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm(instance=membre)
    return render(request, 'membres/form_membre.html', {'form': form, 'titre': 'Modifier le membre'})


@login_required
def archiver_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    membre.actif = False
    membre.save()
    return redirect('liste_membres')


@login_required
def tableau_de_bord(request):
    total_membres = Membre.objects.count()
    membres_actifs = Membre.objects.filter(actif=True).count()
    membres_archives = Membre.objects.filter(actif=False).count()
    cotisations_payees = Cotisation.objects.filter(statut_paiement='paye').count()
    cotisations_impayees = Cotisation.objects.filter(statut_paiement='impaye').count()
    cotisations_attente = Cotisation.objects.filter(statut_paiement='en_attente').count()
    membres_par_fonction = Fonction.objects.annotate(nb=Count('membres')).order_by('-nb')

    return render(request, 'membres/tableau_de_bord.html', {
        'total_membres': total_membres,
        'membres_actifs': membres_actifs,
        'membres_archives': membres_archives,
        'cotisations_payees': cotisations_payees,
        'cotisations_impayees': cotisations_impayees,
        'cotisations_attente': cotisations_attente,
        'membres_par_fonction': membres_par_fonction,
    })
