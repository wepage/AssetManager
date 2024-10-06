from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class CustomUser(AbstractBaseUser):
    #objects = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    pin = models.PositiveIntegerField(unique=True)
    password = models.CharField(max_length=128, blank=True, null=True)  # Password is optional
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'pin'

    def has_perm(self, perm, obj=None):
        # Disable permission system by always returning False
        return False

    def has_module_perms(self, app_label):
        # Disable permission system by always returning False
        return False

    def __str__(self):
        return self.name
