# Generated by Django 5.1.3 on 2025-02-13 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_asset_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
