import unittest
from .. import models
from django.contrib.auth.models import User


class UsersModelsTestCases(unittest.TestCase):
    def test_first_user_profile(self):
        # Setup
        testUsername = 'UsersTestProfile1'
        testUser = None
        testProfile = None
        imageUrl = 'profile_pics/DefaultMan.jpg'
        imageUrlPrefix = '/media/'
        # Run
        if not User.objects.filter(email=testUsername + '@gmail.com').exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Profile.objects.filter(user=testUser).exists():
            testProfile = models.Profile(user=testUser, image=imageUrl)
            testProfile.save()
        else:
            testProfile = models.Profile.objects.get(user=testUser)
        # Check
        self.assertEqual(testProfile, testUser.profile)
        self.assertEqual(imageUrlPrefix + imageUrl, testUser.profile.image.url)

    def test_str(self):
        # Setup
        testUsername = 'UsersTestProfile2'
        testUser = None
        testProfile = None
        imageUrl = 'profile_pics/DefaultMan.jpg'
        profileStr = 'Profile'
        # Run
        if not User.objects.filter(email=testUsername + '@gmail.com').exists():
            testUser = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
        else:
            testUser = User.objects.get(username=testUsername)
        response = User.objects.filter(username=testUsername).first()
        # Check
        self.assertEqual(response, testUser)
        # Run
        if not models.Profile.objects.filter(user=testUser).exists():
            testProfile = models.Profile(user=testUser, image=imageUrl)
            testProfile.save()
        else:
            testProfile = models.Profile.objects.get(user=testUser)
        # Check
        self.assertEqual(testProfile.__str__(), testUsername + profileStr)
