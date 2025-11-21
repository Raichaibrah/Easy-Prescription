from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class LoginViewTest(TestCase):

    def setUp(self):
        # Création d'un utilisateur pour les tests
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_login_valid_user(self):
        # Test de connexion avec des identifiants valides
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        # Vérification de la redirection vers la page d'accueil
        self.assertRedirects(response, reverse('home'))

    def test_login_invalid_user(self):
        # Test de connexion avec des identifiants invalides
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',  # Mauvais mot de passe
        })
        # Vérifiez que des erreurs sont présentes dans le formulaire
        form = response.context.get('form')  # Récupérer le formulaire du contexte de la réponse
        self.assertTrue(form.errors)  # Vérifie que des erreurs sont présentes
        self.assertFormError(response, 'form', None, 'Veuillez corriger les erreurs ci-dessus.')  # Vérification d'une erreur générique dans le formulaire


class LogoutViewTest(TestCase):

    def setUp(self):
        # Création d'un utilisateur pour les tests
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_logout_user(self):
        # Test de déconnexion de l'utilisateur
        self.client.login(username='testuser', password='testpassword')  # Connexion de l'utilisateur
        response = self.client.get(reverse('logout'))  # Déconnexion
        self.assertRedirects(response, reverse('home'))  # Vérifie la redirection après déconnexion


class SignupViewTest(TestCase):

    def test_signup_valid_user(self):
        # Test d'inscription avec des informations valides
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password': 'newpassword',
            'confirm_password': 'newpassword',  # Confirmer le même mot de passe
        })
        # Vérifie que l'utilisateur est redirigé vers la page d'accueil après l'inscription
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())  # Vérifie que l'utilisateur a été créé

    def test_signup_invalid_user(self):
        # Test d'inscription avec des mots de passe non correspondants
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password': 'newpassword',
            'confirm_password': 'differentpassword',  # Mots de passe différents
        })
        self.assertFormError(response, 'form', None, 'Les mots de passe ne correspondent pas.')  # Vérification d'un message d'erreur


class ProfileViewTest(TestCase):

    def setUp(self):
        # Création d'un utilisateur pour les tests
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_profile_view(self):
        # Test de la vue du profil pour un utilisateur connecté
        self.client.login(username='testuser', password='testpassword')  # Connexion de l'utilisateur
        response = self.client.get(reverse('profil'))  # Accéder à la page du profil
        self.assertContains(response, 'testuser')  # Vérifie que le nom d'utilisateur apparaît sur la page

    def test_edit_profile_view(self):
        # Test de la vue de modification du profil
        self.client.login(username='testuser', password='testpassword')  # Connexion de l'utilisateur
        response = self.client.get(reverse('profil') + '?edit=1')  # Accéder à la page d'édition du profil
        self.assertContains(response, 'form')  # Vérifie que le formulaire est présent dans la réponse

    def test_edit_profile_post(self):
        # Test de la soumission d'un formulaire pour modifier le profil
        self.client.login(username='testuser', password='testpassword')  # Connexion de l'utilisateur
        response = self.client.post(reverse('profil'), {
            'username': 'newusername',
            'password': 'newpassword',
            'confirm_password': 'newpassword',
        })
        # Vérifie que le profil a été mis à jour et redirige vers la page de profil
        self.assertRedirects(response, reverse('profil'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')  # Vérifie que le nom d'utilisateur a été mis à jour
