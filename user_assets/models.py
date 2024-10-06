from django.db import models


from assets.models import Asset
from users.models import CustomUser


class UserAsset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_assets')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='asset_users')
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.user.name} assigned {self.asset.name} on {self.assigned_date}"
      #  return f"{self.user.name} assigned {self.asset.name} on {self.assigned_date} by {self.assigned_from.name}"