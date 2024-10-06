from django.db import models


# Create your models here.
class Asset(models.Model):
    asset_group_choices = (
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    group = models.CharField(max_length=10, choices=asset_group_choices, default='Other')

