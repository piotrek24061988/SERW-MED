import unittest, json
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

    def test_json_post(self):
        # Setup
        usernamesJson = None
        newsJson = None
        user = None
        response = None
        # Run
        with open('news/tests/json/users.json') as f:
            usernamesJson = json.load(f)
        with open('news/tests/json/news.json') as f:
            newsJson = json.load(f)
        # Run
        for usernameJson in usernamesJson:
            if not User.objects.filter(username=usernameJson['user']).exists():
                user = User.objects.create_user(usernameJson['user'], usernameJson['user'] + '@gmail.com', '1234')
            else:
                user = User.objects.get(username=usernameJson['user'])
            response = User.objects.filter(username=usernameJson['user']).first()
            # Check
            self.assertEqual(response, user)
            # Run
            for oneNewsJson in newsJson:
                if oneNewsJson['user'] == usernameJson['user']:
                    if not models.News.objects.filter(title=oneNewsJson['title']).exists():
                        post = models.News(title=oneNewsJson['title'], content=oneNewsJson['content'], author_id=user.id)
                        post.save()
                        # Check
                        self.assertEqual(oneNewsJson['title'], models.News.objects.last().title)
                        self.assertEqual(oneNewsJson['content'], models.News.objects.last().content)
                    else:
                        post = models.News.objects.filter(title=oneNewsJson['title']).first()
                        # Check
                        self.assertEqual(oneNewsJson['title'], post.title)


class EmailsModelsTestCases(unittest.TestCase):
    def test_example_emails(self):
        # Setup
        testUsername = 'Email user'
        testEmail = 'test@gmail.com'
        testTitle = 'Email title'
        testContent = 'Email content'
        emails = None
        # Run
        if not models.Emails.objects.filter(title=testTitle).exists():
            # Run
            emails = models.Emails(name=testUsername, email=testEmail, title=testTitle, content=testContent)
            emails.save()
            # Check
            self.assertEqual(testTitle, models.Emails.objects.last().title)
            self.assertEqual(testContent, models.Emails.objects.last().content)
        else:
            # Run
            emails = models.Emails.objects.filter(title=testTitle).first()
            # Check
            self.assertEqual(testTitle, emails.title)
