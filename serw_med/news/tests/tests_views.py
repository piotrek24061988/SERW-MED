import unittest
from .. import views
from django.test import TestCase, Client
from django.urls import reverse


class RequestStub:
    class USER:
        @staticmethod
        def validate_unique(exclude):
            pass

        @staticmethod
        def full_clean(exclude, validate_unique):
            pass

        def is_authenticated(self):
            return True

        class _meta:
            concrete_fields = ''
            private_fields = ''
            many_to_many = ''
            fields = ''

        class profile:
            @staticmethod
            def validate_unique(exclude):
                pass

            @staticmethod
            def full_clean(exclude, validate_unique):
                pass

            class _meta:
                concrete_fields = ''
                private_fields = ''
                many_to_many = ''
                fields = ''

    META = {'CSRF_COOKIE': []}
    user = USER
    method = 'GET'
    POST = {'POST': []}
    FILES = {'FILES': []}


class NewsViewsTestCases(unittest.TestCase):
    # Common setup
    request = RequestStub
    request.method = 'GET'
    response_status = 200

    def test_about(self):
        # Setup
        response_content = b'O nas'
        # Run
        response = views.SerwMed.about(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_contact(self):
        # Setup
        response_content = b'Serwis Aparatury Medycznej SERW-MED'
        # Run
        response = views.SerwMed.contact(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_cooperation(self):
        # Setup
        response_content = b'Franklin Delano Roosvelt'
        # Run
        response = views.SerwMed.cooperation(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_gallery(self):
        # Setup
        response_content = b'gallerySlider'
        # Run
        response = views.SerwMed.gallery(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)


class NewsViewsDjangoTestCases(TestCase):
    # Common setup
    def setUp(self):
        self.client = Client()

    def test_about_GET(self):
        # Setup
        url = reverse('serw-med-about')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_GET(self):
        # Setup
        url = reverse('serw-med-cont')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_POST(self):
        # Setup
        url = reverse('serw-med-cont')
        # Run
        response = self.client.post(url,
        {
            'name': 'piotrek24061988Test',
            'email': 'piotrek24061988@gmail.com',
            'title': 'titleTest',
            'content': 'contentTest'
        })
        # Check
        self.assertEqual(response.status_code, 302)

    def test_contact_POST_EMPTY(self):
        # Setup
        url = reverse('serw-med-cont')
        # Run
        response = self.client.post(url, {})
        # Check
        self.assertEqual(response.status_code, 200)

    def test_cooperation_GET(self):
        # Setup
        url = reverse('serw-med-coop')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cooperation.html')

    def test_gallery_GET(self):
        # Setup
        url = reverse('serw-med-gall')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_news_GET(self):
        # Setup
        url = reverse('serw-med-news')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')

    def test_news_fake_user_GET(self):
        # Setup
        url = reverse('serw-med-news-user', args=['nonExistingUserName-serw-med-news-user'])
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'news.html')

    def test_news_fake_detail_GET(self):
        # Setup
        url = reverse('serw-med-news-detail', args=['999'])
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'news_single.html')

    def test_news_fake_create_GET(self):
        # Setup
        url = reverse('serw-med-news-create')
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'news_create.html')

    def test_news_fake_update_GET(self):
        # Setup
        url = reverse('serw-med-news-update', args=['999'])
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'news_create.html')

    def test_news_fake_delete_GET(self):
        # Setup
        url = reverse('serw-med-news-delete', args=['999'])
        # Run
        response = self.client.get(url)
        # Check
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'news_delete.html')