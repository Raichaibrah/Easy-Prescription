from django.test import TestCase
from django.urls import reverse
from pharmacies.models import Pharmacie

class PharmacieViewTest(TestCase):

    def setUp(self):
        # Création de quelques pharmacies pour les tests
        self.pharmacie1 = Pharmacie.objects.create(nom='Pharmacie 1', ville='Paris', description='Pharmacie à Paris')
        self.pharmacie2 = Pharmacie.objects.create(nom='Pharmacie 2', ville='Paris', description='Pharmacie à Paris')

    def test_search_pharmacies(self):
        # Test de recherche de pharmacies par ville
        response = self.client.get(reverse('search_pharmacies'), {'ville': 'Paris'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pharmacie 1')
        self.assertContains(response, 'Pharmacie 2')

    def test_no_pharmacies_found(self):
        # Test quand aucune pharmacie n'est trouvée pour une ville
        response = self.client.get(reverse('search_pharmacies'), {'ville': 'NonExist'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aucune pharmacie trouvée')
