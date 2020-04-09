from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='news_pics', storage=OverwriteStorage(), null=True)
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
