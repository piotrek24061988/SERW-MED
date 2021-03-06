from django.test import TransactionTestCase
from .. import forms


class CustomAuthenticationFormDjangoTestCases(TransactionTestCase):
    def setUp(self):
        self.username = 'UsersTestProfile123456789'
        self.password = '@!XZVSGSDF'

    def test_custom_authentication_form_invalid(self):
        # Run
        form = forms.CustomAuthenticationForm(
            data={
                'username': self.username  # missing password
            })
        # Check
        self.assertFalse(form.is_valid())


class CustomSetPasswordFormDjangoTestCases(TransactionTestCase):
    def setUp(self):
        self.password = '@!XZVSGSDF'

    def test_custom_set_password_form_valid(self):
        # Run
        form = forms.CustomSetPasswordForm(user=None,
            data={
                'new_password1': self.password,
                'new_password2': self.password
            })
        # Check
        self.assertTrue(form.is_valid())
        print(form.errors)

    def test_custom_set_password_form_invalid(self):
        # Run
        form = forms.CustomSetPasswordForm(user=None,
            data={
                'new_password1': self.password  # missing new_password2
            })
        # Check
        self.assertFalse(form.is_valid())


class UserUpdateFormDjangoTestCases(TransactionTestCase):
    def setUp(self):
        self.username = 'UsersTestProfile123456789'
        self.email = 'UsersTestProfile123456789@gmail.com'

    def test_user_update_form_valid(self):
        # Run
        form = forms.UserUpdateForm(
            data={
                'username': self.username,
                'email': self.email
            })
        # Check
        self.assertTrue(form.is_valid())
        print(form.errors)

    def test_user_update_form_valid(self):
        # Run
        form = forms.UserUpdateForm(
            data={
                'username': self.username + '123'  # missing email
            })
        # Check
        self.assertFalse(form.is_valid())


class UserRegisterFormDjangoTestCases(TransactionTestCase):
    def setUp(self):
        self.username = 'UsersTestProfile1ABCDEF'
        self.email = 'UsersTestProfile1ABCDEF@gmail.com'
        self.password = 'UTP1234@!'

    def test_user_register_form_valid(self):
        # Run
        form = forms.UserRegisterForm(
            data={
                'username': self.username,
                'email': self.email,
                'password1': self.password,
                'password2': self.password
            })
        # Check
        self.assertTrue(form.is_valid())
        print(form.errors)

    def test_user_register_form_invalid(self):
        # Run
        form = forms.UserRegisterForm(
            data={
                'username': self.username,
                'email': self.email,
                'password1': self.password  # missing password2
            })
        # Check
        self.assertFalse(form.is_valid())


class ProfileUpdateFormDjangoTestCases(TransactionTestCase):
    def test_profile_update_form_invalid(self):
        # Run
        form = forms.ProfileUpdateForm(data={})
        # Check
        self.assertFalse(form.is_valid())