import unittest
from django.contrib.auth.models import User
from .. import models


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
            user = None
            news = None
            # Run
            if not User.objects.filter(username=testUsername).exists():
                user = User.objects.create_user(testUsername, testUsername + '@gmail.com', '1234')
            else:
                user = User.objects.get(username=testUsername)
            response = User.objects.filter(username=testUsername).first()
            # Check
            self.assertEqual(response, user)
            # Run
            if not models.News.objects.filter(title=testTitle).exists():
                # Run
                news = models.News(title=testTitle, content=testContent, author_id=i)
                news.save()
                # Check
                self.assertEqual(testTitle, models.News.objects.last().title)
                self.assertEqual(testContent, models.News.objects.last().content)
            else:
                # Run
                news = models.News.objects.filter(title=testTitle).first()
                # Check
                self.assertEqual(testTitle, news.title)
