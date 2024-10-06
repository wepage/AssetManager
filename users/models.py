from django.db import models

# Create your models here.
class Users(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    pin = models.IntegerField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
