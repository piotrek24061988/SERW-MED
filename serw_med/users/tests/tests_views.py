import unittest
from .. import views


class RequestStub:
    class USER:
        def is_authenticated(self):
            return True

        class _meta:
            concrete_fields = ''
            private_fields = ''
            many_to_many = ''


        class profile:
            class _meta:
                concrete_fields = ''
                private_fields = ''
                many_to_many = ''

    META = {'CSRF_COOKIE': []}
    user = USER
    method = 'POST'
    POST = {'POST': []}


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