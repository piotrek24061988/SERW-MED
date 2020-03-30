import unittest
from .. import models
from django.contrib.auth.models import User


class NewsModelsTestCases(unittest.TestCase):
    def test_user_empty(self):
        # Setup
        user = None
        # Run
        response = User.objects.filter(username=user).first()
        # Check
        self.assertEqual(response, user)

    def test_example_news(self):
        for i in [1, 2, 3]:
            # Setup
            testUsername = 'News user' + str(i)
            testTitle = 'News title' + str(i)
            testContent = 'News content' + str(i)
            # Run
            if not User.objects.filter(email=testUsername + '@gmail.com').exists():
                user = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
            else:
                user = User.objects.get(username=testUsername)
            response = User.objects.filter(username=testUsername).first()
            # Check
            self.assertEqual(response, user)
            # Run
            news = models.News(title=testTitle, content=testContent, author_id=i)
            news.save()
            # Check
            self.assertEqual(testTitle, models.News.objects.last().title)
            self.assertEqual(testContent, models.News.objects.last().content)
