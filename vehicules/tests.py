from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Client, Vehicule


class VehiculeTests(TestCase):

    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        # Connexion de l'utilisateur
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        # Création d'un client
        self.client_garage = Client.objects.create(
            nom="Jean Dupont",
            email="jean@gmail.com"
        )

        # Création d'un véhicule
        self.vehicule = Vehicule.objects.create(
            plaque="AB-123-CD",
            marque="Peugeot",
            modele="208",
            annee=2022,
            client=self.client_garage
        )

    def test_liste_vehicules(self):
        response = self.client.get(
            reverse("liste_vehicules")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AB-123-CD")
        self.assertContains(response, "Peugeot")
        self.assertContains(response, "208")

    def test_ajouter_vehicule(self):
        response = self.client.post(
            reverse("ajouter_vehicule"),
            {
                "plaque": "CD-456-EF",
                "marque": "Renault",
                "modele": "Clio",
                "annee": "2023",
                "client": self.client_garage.id,
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Vehicule.objects.filter(
                plaque="CD-456-EF"
            ).exists()
        )

    def test_modifier_vehicule(self):
        response = self.client.post(
            reverse(
                "modifier_vehicule",
                args=[self.vehicule.id]
            ),
            {
                "plaque": "AB-999-CD",
                "marque": "Citroen",
                "modele": "C3",
                "annee": "2024",
                "client": self.client_garage.id,
            }
        )

        self.assertEqual(response.status_code, 302)

        self.vehicule.refresh_from_db()

        self.assertEqual(
            self.vehicule.plaque,
            "AB-999-CD"
        )

        self.assertEqual(
            self.vehicule.marque,
            "Citroen"
        )

        self.assertEqual(
            self.vehicule.modele,
            "C3"
        )

        self.assertEqual(
            self.vehicule.annee,
            2024
        )

    def test_supprimer_vehicule(self):
        response = self.client.post(
            reverse(
                "supprimer_vehicule",
                args=[self.vehicule.id]
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Vehicule.objects.filter(
                id=self.vehicule.id
            ).exists()
        )


class ClientTests(TestCase):

    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        # Connexion de l'utilisateur
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        # Création d'un client
        self.client_garage = Client.objects.create(
            nom="Marie Martin",
            email="marie@gmail.com"
        )

    def test_liste_clients(self):
        response = self.client.get(
            reverse("liste_clients")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Marie Martin")

    def test_ajouter_client(self):
        response = self.client.post(
            reverse("ajouter_client"),
            {
                "nom": "Paul Durand",
                "email": "paul@gmail.com",
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Client.objects.filter(
                nom="Paul Durand"
            ).exists()
        )

    def test_modifier_client(self):
        response = self.client.post(
            reverse(
                "modifier_client",
                args=[self.client_garage.id]
            ),
            {
                "nom": "Marie Martin Modifiee",
                "email": "nouveau@gmail.com",
            }
        )

        self.assertEqual(response.status_code, 302)

        self.client_garage.refresh_from_db()

        self.assertEqual(
            self.client_garage.nom,
            "Marie Martin Modifiee"
        )

        self.assertEqual(
            self.client_garage.email,
            "nouveau@gmail.com"
        )

    def test_supprimer_client(self):
        response = self.client.post(
            reverse(
                "supprimer_client",
                args=[self.client_garage.id]
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Client.objects.filter(
                id=self.client_garage.id
            ).exists()
        )