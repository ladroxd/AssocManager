# AssociationManager — Instructions Claude

## Langue
- L'utilisateur communique en **anglais**.
- Tout le code produit (noms de variables, fonctions, classes, commentaires, messages UI, chaînes de texte, etc.) doit être en **français**.
- Les réponses de Claude peuvent rester en anglais sauf demande contraire.

---

## Présentation du Projet
Application web **Python / Django** de gestion des membres d'une association (AssocManager).  
Deux types d'utilisateurs : **Admin** (Bureau de l'association) et **Membre** (consultation annuaire).

---

## Fonctionnalités Principales
1. **Gestion des adhésions** — enregistrer, modifier, archiver, lister les membres.
2. **Recherche & Filtrage** — par nom, par fonction (Président, Secrétaire, Bénévole…), par niveau de scolarité.
3. **Suivi des profils** — ancienneté calculée depuis `date_inscription`, classement par niveau d'études.
4. **Annuaire interactif** — liste de contacts (téléphone, email) pour communication interne.

---

## Architecture des Données (Modèles Django)

| Modèle | Champs |
|---|---|
| `Membre` | `nom`, `prenom`, `telephone`, `email`, `fonction` (FK), `date_inscription`, `niveau_scolarite` |
| `Fonction` | `titre_poste`, `responsabilite` |
| `Cotisation` | `membre` (FK), `annee`, `montant`, `statut_paiement` |

Base de données : **MySQL** (via phpMyAdmin).

---

## Spécifications Techniques
- **Framework** : Django
- **Frontend** : Bootstrap (responsive — cartes ou tableaux stylisés)
- **Admin Django** : interface `/admin` configurée pour export et modification rapide des membres

---

## Livrables Attendus
- Code source complet (GitHub + dossier compressé)
- Rapport écrit détaillant la structure du projet
- Présentation PowerPoint

---

## Instructions à venir
*(Les instructions supplémentaires seront ajoutées ici au fur et à mesure.)*
