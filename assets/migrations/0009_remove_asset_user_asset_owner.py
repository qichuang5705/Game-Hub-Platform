# Generated by Django 5.1.3 on 2025-02-22 05:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_alter_purchase_asset_delete_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='User',
        ),
        migrations.AddField(
            model_name='asset',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to=settings.AUTH_USER_MODEL),
        ),
    ]
