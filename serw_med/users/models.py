from django.db import models
from django.contrib.auth.models import User
from common import storage


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/DefaultMan.jpg', upload_to='profile_pics', storage=storage.OverwriteStorage())

    def __str__(self):
        return f'{self.user.username}Profile'
