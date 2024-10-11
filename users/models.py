from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    pin = models.PositiveIntegerField(unique=True)
    password = models.CharField(max_length=128, blank=True, null=True)  # Password is optional
    is_active = models.BooleanField(default=False) # when user profile is not complete
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
