# Generated by Django 3.0.4 on 2020-03-31 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='users',
            new_name='user',
        ),
    ]
