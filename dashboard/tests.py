from django.test import TestCase
from django.urls import reverse
from dashboard.models import DashboardData

class DashboardViewTest(TestCase):

    def setUp(self):
        # Création de quelques données pour le tableau de bord
        self.data1 = DashboardData.objects.create(title='Data 1', content='Content 1')
        self.data2 = DashboardData.objects.create(title='Data 2', content='Content 2')

    def test_dashboard_view(self):
        # Test d'affichage du tableau de bord
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Data 1')
        self.assertContains(response, 'Content 1')
        self.assertContains(response, 'Data 2')
        self.assertContains(response, 'Content 2')

    def test_search_dashboard_data(self):
        # Test de la recherche dans le tableau de bord
        response = self.client.get(reverse('dashboard'), {'query': 'Data 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Data 1')
        self.assertNotContains(response, 'Data 2')
