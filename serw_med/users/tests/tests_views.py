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
    method = 'POST'
    POST = {'POST': []}
    FILES = {'FILES': []}


class UsersViewsTestCases(unittest.TestCase):
    def test_register(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Rejestracja'
        # Run
        response = views.SerwMedUsers.register(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_profile_get(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Informacje o profilu'
        # Run
        request.method = 'GET'
        response = views.SerwMedUsers.profile(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)

    def test_profile_post(self):
        # Setup
        request = RequestStub
        response_status = 200
        response_content = b'Informacje o profilu'
        # Run
        request.method = 'POST'
        response = views.SerwMedUsers.profile(request)
        # Check
        self.assertEqual(response.status_code, response_status)
        self.assertIn(response_content, response.content)
