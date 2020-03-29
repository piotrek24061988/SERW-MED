import unittest
from .. import views


class NewsViewsTestCases(unittest.TestCase):
    # Common setup
    request = 'fake request'
    response_status = 200

    def test_news(self):
        # Setup
        response_content = b'News user'
        # Run
        response = views.SerwMed.news(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_about(self):
        # Setup
        response_content = b'News1'
        # Run
        response = views.SerwMed.about(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_about(self):
        # Setup
        response_content = b'SERW-MED ABOUT'
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
        response_content = b'SERW-MED COOPERATION'
        # Run
        response = views.SerwMed.cooperation(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_gallery(self):
        # Setup
        response_content = b'SERW-MED GALLERY'
        # Run
        response = views.SerwMed.gallery(NewsViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, NewsViewsTestCases.response_status)
        self.assertIn(response_content, response.content)
