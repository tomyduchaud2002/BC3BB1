from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    plaque = models.CharField(max_length=20, unique=True)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField(null=True, blank=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vehicules"
    )

    def __str__(self):
        return f"{self.marque} {self.modele} - {self.plaque}"