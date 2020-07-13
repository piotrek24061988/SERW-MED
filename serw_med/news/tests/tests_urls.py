import unittest
from django.urls import reverse, resolve
from .. import views


class NewsUrlsTestCases(unittest.TestCase):

    def test_url_about(self):
        # Setup
        url = reverse('serw-med-about')
        testFunc = views.SerwMed.about
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_news(self):
        # Setup
        url = reverse('serw-med-news')
        testClass = views.NewsListView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_user(self):
        # Setup
        url = reverse('serw-med-news-user', args=['0'])
        testClass = views.UserNewsListView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_detail(self):
        # Setup
        url = reverse('serw-med-news-detail', args=['0'])
        testClass = views.NewsDetailView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_create(self):
        # Setup
        url = reverse('serw-med-news-create')
        testClass = views.NewsCreateView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_update(self):
        # Setup
        url = reverse('serw-med-news-update', args=['0'])
        testClass = views.NewsUpdateView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_delete(self):
        # Setup
        url = reverse('serw-med-news-delete', args=['0'])
        testClass = views.NewsDeleteView
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func.view_class, testClass)

    def test_url_contact(self):
        # Setup
        url = reverse('serw-med-cont')
        testFunc = views.SerwMed.contact
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_cooperation(self):
        # Setup
        url = reverse('serw-med-coop')
        testFunc = views.SerwMed.cooperation
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)

    def test_url_gallery(self):
        # Setup
        url = reverse('serw-med-gall')
        testFunc = views.SerwMed.gallery
        # Run
        resolvedUrl = resolve(url)
        # Check
        self.assertEqual(resolvedUrl.func, testFunc)