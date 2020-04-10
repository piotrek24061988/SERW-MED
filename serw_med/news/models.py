from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from common import storage


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='news_pics', storage=storage.OverwriteStorage(), null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "title: " + self.title + ", content: " + self.content

    def get_absolute_url(self):
        return reverse('serw-med-news-detail', kwargs={'pk': self.pk})


class Emails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "name: " + self.name + ", email: " + self.email + ", title: " + self.title
