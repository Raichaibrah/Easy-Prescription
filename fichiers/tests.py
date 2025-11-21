from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from fichiers.models import Ordonnance
from fichiers.storage import GoogleDriveStorage

class OrdonnanceViewTest(TestCase):

    def setUp(self):
        # Créer un utilisateur
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        # Créer une ordonnance pour cet utilisateur
        self.ordonnance = Ordonnance.objects.create(user=self.user, name='Test Ordonnance', file='dummyfile.pdf')

    def test_create_ordonnance(self):
        # Test de la création d'une ordonnance par un utilisateur
        self.client.login(username='testuser', password='testpassword')  # Connexion
        response = self.client.post(reverse('create_ordonnance'), {
            'name': 'New Ordonnance',
            'file': 'newfile.pdf'
        })
        self.assertRedirects(response, reverse('historique_ordonnances'))
        self.assertTrue(Ordonnance.objects.filter(name='New Ordonnance').exists())  # Vérifier que l'ordonnance a été créée

    def test_delete_ordonnance(self):
        # Test de la suppression d'une ordonnance
        self.client.login(username='testuser', password='testpassword')  # Connexion
        response = self.client.post(reverse('supprimer_ordonnance', args=[self.ordonnance.id]))
        self.assertRedirects(response, reverse('historique_ordonnances'))
        self.assertFalse(Ordonnance.objects.filter(id=self.ordonnance.id).exists())  # Vérifier que l'ordonnance a été supprimée

    def test_delete_ordonnance_not_owner(self):
        # Test de suppression par un utilisateur qui n'est pas le propriétaire de l'ordonnance
        another_user = get_user_model().objects.create_user(username='otheruser', password='otherpassword')
        self.client.login(username='otheruser', password='otherpassword')
        response = self.client.post(reverse('supprimer_ordonnance', args=[self.ordonnance.id]))
        self.assertEqual(response.status_code, 403)  # L'utilisateur n'est pas autorisé à supprimer
