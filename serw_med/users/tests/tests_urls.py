import unittest
from django.urls import reverse, resolve
from .. import views
from django.contrib.auth import views as auth_views


class NewsUrlsTestCases(unittest.TestCase):

    def test_url_register(self):
        # Setup
        url = reverse('serw-med-register')
        testFunc = views.SerwMedUsers.register
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_login(self):
        # Setup
        url = reverse('serw-med-login')
        testClass = views.CustomLoginView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_logout(self):
        # Setup
        url = reverse('serw-med-logout')
        testClass = auth_views.LogoutView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_profile(self):
        # Setup
        url = reverse('serw-med-profile')
        testFunc = views.SerwMedUsers.profile
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_password_reset(self):
        # Setup
        url = reverse('password_reset')
        testClass = auth_views.PasswordResetView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_password_reset_done(self):
        # Setup
        url = reverse('password_reset_done')
        testClass = auth_views.PasswordResetDoneView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_password_reset_confirm(self):
        # Setup
        url = reverse('password_reset_confirm', args=['0', '1'])
        testClass = views.CustomSetPasswordView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_password_reset_complete(self):
        # Setup
        url = reverse('password_reset_complete')
        testClass = auth_views.PasswordResetCompleteView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)