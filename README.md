# Garage Automobile — Auth uniquement

Projet Django minimal pour un garage automobile, avec pages de connexion et réinitialisation de mot de passe. Stack: HTML/CSS/JS, Python/Django, MySQL (via Docker), fallback SQLite.

## Prérequis
- macOS avec Python 3.13
- `pip`
- (Optionnel) Docker Desktop pour MySQL

## Installation des dépendances
1. Créer et activer l’environnement virtuel:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Installer les dépendances:
   ```bash
   pip install -r requirements.txt
   ```

## Démarrage rapide (SQLite)
1. Copier l’exemple d’environnement:
   ```bash
   cp .env.example .env
   ```
   Laisse `MYSQL_NAME` vide pour utiliser SQLite.
2. Appliquer les migrations:
   ```bash
   source .venv/bin/activate
   python manage.py migrate
   ```
3. Créer un superutilisateur (interactif):
   ```bash
   python manage.py createsuperuser
   ```
   Ou utiliser l’admin pré-configuré (si SQLite déjà généré):
   - Utilisateur: `admin`
   - Mot de passe: `GarageAdmin!234`
4. Lancer le serveur:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
5. Ouvrir: `http://0.0.0.0:8000/` (redirige vers connexion).

## Utiliser MySQL via Docker
1. Lancer Docker Desktop.
2. Démarrer la base:
   ```bash
   docker compose up -d --wait
   ```
3. Configurer `.env`:
   ```env
   MYSQL_NAME=garage_db
   MYSQL_USER=garage_user
   MYSQL_PASSWORD=motdepasse
   MYSQL_HOST=127.0.0.1
   MYSQL_PORT=3306
   ```
4. Appliquer les migrations:
   ```bash
   source .venv/bin/activate
   python manage.py migrate
   ```
5. Créer un superutilisateur (la base MySQL est vide au départ):
   ```bash
   python manage.py createsuperuser
   ```
6. Lancer le serveur:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Authentification & Mot de passe oublié
- Connexion: `http://0.0.0.0:8000/accounts/login/`
- Déconnexion: via le lien sur la page d’accueil.
- Mot de passe oublié: lien "Mot de passe oublié ?" sur la page de connexion.
- En dev, les emails sont affichés dans la console (backend email console).

## Variables d’environnement
- Fichier `.env` chargé via `python-dotenv`. Si `MYSQL_NAME` est vide, SQLite est utilisé.
- Exemple disponible dans `.env.example`.

## Arborescence
- `garage_site/settings.py`: config DB (MySQL/SQLite), templates, statiques, email.
- `garage_site/urls.py`: routes `home` + `django.contrib.auth.urls`.
- `garage_site/views.py`: vue d’accueil protégée.
- `templates/registration/*.html`: pages d’auth et reset.
- `static/css/style.css`, `static/js/main.js`: assets.
- `docker-compose.yml`: MySQL de dev.
- `scripts/set_admin_password.py`: script pour fixer le mot de passe admin.

## Dépannage
- Erreur balise `{% static %}`: assure-toi que les templates contiennent `{% load static %}`.
- MySQL "Connection refused": démarre Docker Desktop et `docker compose up`.
- Problèmes de dépendances: `pip install -r requirements.txt` dans l’environnement virtuel.

## Licence
Projet éducatif (bloc blanc) — usage pédagogique.

CODE BC3BB1

Documentation généré par IA avec Trae.