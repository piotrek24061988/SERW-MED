from django.test import TestCase, Client
from django.urls import reverse


class UsersViewsDjangoTestCases(TestCase):
    # Common setup
    def setUp(self):
        self.client = Client()

    def test_register_GET(self):
        # Setup
        url = reverse('serw-med-register')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_POST(self):
        # Setup
        url = reverse('serw-med-register')
        # Run
        response = self.client.post(url,
        {
            'username': 'tesgisterTest',
            'email': 'tesgisterTest@gmail.com',
            'password1': '1234ABCD',
            'password2': '1234ABCD'
        })
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_GET(self):
        # Setup
        url = reverse('serw-med-login')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_GET(self):
        # Setup
        url = reverse('serw-med-logout')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logout.html')

    def test_fake_profile_GET(self):
        # Setup
        url = reverse('serw-med-profile')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'profile.html')

    def test_password_reset_GET(self):
        # Setup
        url = reverse('password_reset')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_reset.html')

    def test_password_reset_done_GET(self):
        # Setup
        url = reverse('password_reset_done')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_reset_done.html')

    def test_password_reset_complete_GET(self):
        # Setup
        url = reverse('password_reset_complete')
        # Run
        response = self.client.get(url, args=['999', '999'])
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_reset_complete.html')