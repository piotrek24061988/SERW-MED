import unittest
from .. import views


class NewsViewsTestCases(unittest.TestCase):
    def test_home(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = views.NewsViews.homeHTML()
        # Run
        response = views.NewsViews.home(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_about(self):
        # Setup
        request = 'fake request'
        response_status = 200
        response_content = views.NewsViews.aboutHTML()
        # Run
        response = views.NewsViews.about(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

