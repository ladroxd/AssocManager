# AssocManager

> Application web de gestion des membres d'une association — Django + Bootstrap  
> Web application for managing association members — Django + Bootstrap

---

## 🇫🇷 Version Française

### Présentation
AssocManager est une application web développée avec **Python / Django** permettant de gérer les membres d'une association. Elle offre deux niveaux d'accès : l'**Admin** (Bureau de l'association) et le **Membre** (consultation de l'annuaire).

### Fonctionnalités
- **Annuaire interactif** — consultation publique des membres actifs avec recherche par nom, fonction et niveau de scolarité
- **Gestion des membres** — ajouter, modifier, archiver les membres (Admin uniquement)
- **Tableau de bord** — statistiques en temps réel : membres actifs/archivés, cotisations payées/impayées
- **Authentification** — connexion sécurisée pour l'accès à l'espace d'administration

### Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/ladroxd/AssocManager.git
cd AssocManager

# 2. Installer les dépendances
pip install django mysqlclient

# 3. Configurer la base de données MySQL dans assocmanager/settings.py

# 4. Appliquer les migrations
python manage.py migrate

# 5. Créer un compte administrateur
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

### Structure du Projet
```
AssocManager/
├── assocmanager/        # Configuration Django (settings, urls)
├── membres/             # Application principale
│   ├── models.py        # Modèles : Membre, Fonction, Cotisation
│   ├── views.py         # Vues : annuaire, tableau de bord, CRUD membres
│   ├── forms.py         # Formulaires
│   ├── urls.py          # Routes
│   └── templates/       # Templates HTML (Bootstrap)
└── static/              # Fichiers statiques (images, CSS)
```

### Modèles de Données
| Modèle | Champs |
|---|---|
| `Membre` | nom, prénom, téléphone, email, fonction, date_inscription, niveau_scolarite, actif |
| `Fonction` | titre_poste, responsabilite |
| `Cotisation` | membre, annee, montant, statut_paiement |

### Accès
| URL | Description | Accès |
|---|---|---|
| `/` | Annuaire des membres | Public |
| `/connexion/` | Page de connexion | Public |
| `/tableau-de-bord/` | Tableau de bord admin | Admin |
| `/membres/` | Gestion des membres | Admin |
| `/admin/` | Interface Django Admin | Admin |

---

## 🇬🇧 English Version

### Overview
AssocManager is a web application built with **Python / Django** for managing association members. It provides two access levels: **Admin** (Association Board) and **Member** (directory consultation).

### Features
- **Interactive directory** — public browsing of active members with search by name, role, and education level
- **Member management** — add, edit, archive members (Admin only)
- **Dashboard** — real-time statistics: active/archived members, paid/unpaid contributions
- **Authentication** — secure login for admin access

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ladroxd/AssocManager.git
cd AssocManager

# 2. Install dependencies
pip install django mysqlclient

# 3. Configure MySQL database in assocmanager/settings.py

# 4. Apply migrations
python manage.py migrate

# 5. Create an admin account
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver
```

### Project Structure
```
AssocManager/
├── assocmanager/        # Django config (settings, urls)
├── membres/             # Main app
│   ├── models.py        # Models: Membre, Fonction, Cotisation
│   ├── views.py         # Views: directory, dashboard, member CRUD
│   ├── forms.py         # Forms
│   ├── urls.py          # URL routes
│   └── templates/       # HTML templates (Bootstrap)
└── static/              # Static files (images, CSS)
```

### Data Models
| Model | Fields |
|---|---|
| `Membre` | nom, prenom, telephone, email, fonction, date_inscription, niveau_scolarite, actif |
| `Fonction` | titre_poste, responsabilite |
| `Cotisation` | membre, annee, montant, statut_paiement |

### Routes
| URL | Description | Access |
|---|---|---|
| `/` | Member directory | Public |
| `/connexion/` | Login page | Public |
| `/tableau-de-bord/` | Admin dashboard | Admin |
| `/membres/` | Member management | Admin |
| `/admin/` | Django Admin panel | Admin |

---

**Stack** : Python · Django · MySQL · Bootstrap 5
