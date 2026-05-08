from django.urls import path
from . import views

urlpatterns = [
    path('', views.annuaire, name='annuaire'),
    path('tableau-de-bord/', views.tableau_de_bord, name='tableau_de_bord'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/ajouter/', views.ajouter_membre, name='ajouter_membre'),
    path('membres/<int:pk>/', views.detail_membre, name='detail_membre'),
    path('membres/<int:pk>/modifier/', views.modifier_membre, name='modifier_membre'),
    path('membres/<int:pk>/archiver/', views.archiver_membre, name='archiver_membre'),
]
