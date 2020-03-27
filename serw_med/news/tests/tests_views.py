import unittest
from .. import views


class NewsViewsTestCases(unittest.TestCase):
    def test_news(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'PiotrG'
        # Run
        response = views.SerwMed.news(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_about(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'News1'
        # Run
        response = views.SerwMed.about(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_about(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'SERW-MED ABOUT'
        # Run
        response = views.SerwMed.about(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_contact(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'SERW-MED CONTACT'
        # Run
        response = views.SerwMed.contact(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_cooperation(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'SERW-MED COOPERATION'
        # Run
        response = views.SerwMed.cooperation(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_gallery(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = b'SERW-MED GALLERY'
        # Run
        response = views.SerwMed.gallery(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

