import unittest
from .. import views


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
