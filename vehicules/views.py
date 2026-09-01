from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Vehicule, Client


# =========================
# VEHICULES
# =========================

@login_required
def liste_vehicules(request):
    vehicules = Vehicule.objects.select_related("client").all()

    return render(request, "vehicules/liste.html", {
        "vehicules": vehicules
    })


@login_required
def ajouter_vehicule(request):
    clients = Client.objects.all()

    if request.method == "POST":
        plaque = request.POST.get("plaque")
        marque = request.POST.get("marque")
        modele = request.POST.get("modele")
        annee = request.POST.get("annee")
        client_id = request.POST.get("client")

        Vehicule.objects.create(
            plaque=plaque,
            marque=marque,
            modele=modele,
            annee=annee if annee else None,
            client_id=client_id if client_id else None
        )

        return redirect("liste_vehicules")

    return render(request, "vehicules/ajouter.html", {
        "clients": clients
    })


@login_required
def modifier_vehicule(request, id):
    vehicule = get_object_or_404(Vehicule, id=id)
    clients = Client.objects.all()

    if request.method == "POST":
        vehicule.plaque = request.POST.get("plaque")
        vehicule.marque = request.POST.get("marque")
        vehicule.modele = request.POST.get("modele")

        annee = request.POST.get("annee")
        vehicule.annee = annee if annee else None

        client_id = request.POST.get("client")
        vehicule.client_id = client_id if client_id else None

        vehicule.save()

        return redirect("liste_vehicules")

    return render(request, "vehicules/modifier.html", {
        "vehicule": vehicule,
        "clients": clients
    })


@login_required
def supprimer_vehicule(request, id):
    vehicule = get_object_or_404(Vehicule, id=id)

    if request.method == "POST":
        vehicule.delete()
        return redirect("liste_vehicules")

    return render(request, "vehicules/supprimer.html", {
        "vehicule": vehicule
    })


# =========================
# CLIENTS
# =========================

@login_required
def liste_clients(request):
    clients = Client.objects.all()

    return render(request, "vehicules/clients.html", {
        "clients": clients
    })


@login_required
def ajouter_client(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        email = request.POST.get("email")

        Client.objects.create(
            nom=nom,
            email=email
        )

        return redirect("liste_clients")

    return render(request, "vehicules/ajouter_client.html")


@login_required
def modifier_client(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == "POST":
        client.nom = request.POST.get("nom")
        client.email = request.POST.get("email")

        client.save()

        return redirect("liste_clients")

    return render(request, "vehicules/modifier_client.html", {
        "client": client
    })


@login_required
def supprimer_client(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == "POST":
        client.delete()
        return redirect("liste_clients")

    return render(request, "vehicules/supprimer_client.html", {
        "client": client
    })