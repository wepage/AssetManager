# Generated by Django 3.2 on 2024-10-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
