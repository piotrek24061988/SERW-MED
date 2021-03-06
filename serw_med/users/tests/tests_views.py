import unittest
from .. import views
from common import stubs


class UsersViewsTestCases(unittest.TestCase):
    # Common setup
    request = stubs.RequestStub
    response_status = 200

    def test_register(self):
        # Setup
        UsersViewsTestCases.request.method = 'POST'
        response_content = b'Rejestracja'
        # Run
        response = views.SerwMedUsers.register(UsersViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, UsersViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_profile_get(self):
        # Setup
        UsersViewsTestCases.request.method = 'GET'
        response_content = b'Informacje o profilu'
        # Run
        response = views.SerwMedUsers.profile(UsersViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, UsersViewsTestCases.response_status)
        self.assertIn(response_content, response.content)

    def test_profile_post(self):
        # Setup
        UsersViewsTestCases.request.method = 'POST'
        response_content = b'Informacje o profilu'
        # Run
        response = views.SerwMedUsers.profile(UsersViewsTestCases.request)
        # Check
        self.assertEqual(response.status_code, UsersViewsTestCases.response_status)
        self.assertIn(response_content, response.content)