from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "title: " + self.title + ", content: " + self.content

    def get_absolute_url(self):
        return reverse('serw-med-news-detail', kwargs={'pk': self.pk})
