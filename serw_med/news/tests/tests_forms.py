from django.test import SimpleTestCase
from .. import forms


class NewsFormsDjangoTestCases(SimpleTestCase):
    def setUp(self):
        self.testTitle = 'Company Cvid-19 Lockdown'
        self.testContent = 'Since 01.07.2020 company is partially locked down because of covid-19 issue'

    def test_news_create_form_valid(self):
        # Run
        form = forms.NewsCreateForm(
            data={
                'title': self.testTitle,
                'content': self.testContent
            })
        # Check
        self.assertTrue(form.is_valid())

    def test_news_create_form_invalid(self):
        # Run
        form = forms.NewsCreateForm(
            data={
                'title': self.testTitle  # missing content
            })
        # Check
        self.assertFalse(form.is_valid())


class SendEmailFormsDjangoTestCases(SimpleTestCase):
    def setUp(self):
        self.name = 'piotrek24061988'
        self.email = 'piotrek24061988@gmail.com'
        self.testTitle = 'Company Cvid-19 Lockdown'
        self.testContent = 'Since 01.07.2020 company is partially locked down because of covid-19 issue'

    def test_send_email_form_valid(self):
        # Run
        form = forms.SendEmailForm(
            data={
                'name': self.name,
                'email': self.email,
                'title': self.testTitle,
                'content': self.testContent
            })
        # Check
        self.assertTrue(form.is_valid())

    def test_send_email_form_invalid(self):
        # Run
        form = forms.SendEmailForm(
            data={
                'name': self.name,
                'email': self.email,
                'title': self.testTitle  # missing content
            })
        # Check
        self.assertFalse(form.is_valid())
