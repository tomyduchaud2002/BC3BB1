from django.contrib import admin
from django.urls import path, include
from . import views

from vehicules.views import (
    liste_vehicules,
    ajouter_vehicule,
    modifier_vehicule,
    supprimer_vehicule,
    liste_clients,
    ajouter_client,
    modifier_client,
    supprimer_client,
)


urlpatterns = [
    # Accueil
    path("", views.home, name="home"),

    # Authentification
    path("accounts/", include("django.contrib.auth.urls")),

    # Administration
    path("admin/", admin.site.urls),

    # =========================
    # VEHICULES
    # =========================

    path(
        "vehicules/",
        liste_vehicules,
        name="liste_vehicules"
    ),

    path(
        "vehicules/ajouter/",
        ajouter_vehicule,
        name="ajouter_vehicule"
    ),

    path(
        "vehicules/modifier/<int:id>/",
        modifier_vehicule,
        name="modifier_vehicule"
    ),

    path(
        "vehicules/supprimer/<int:id>/",
        supprimer_vehicule,
        name="supprimer_vehicule"
    ),

    # =========================
    # CLIENTS
    # =========================

    path(
        "clients/",
        liste_clients,
        name="liste_clients"
    ),

    path(
        "clients/ajouter/",
        ajouter_client,
        name="ajouter_client"
    ),

    path(
        "clients/modifier/<int:id>/",
        modifier_client,
        name="modifier_client"
    ),

    path(
        "clients/supprimer/<int:id>/",
        supprimer_client,
        name="supprimer_client"
    ),
]