# Generated by Django 5.1.4 on 2025-02-16 18:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0002_framechat_alter_tabelrewards_framechat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TabelRewards',
            new_name='TableRewards',
        ),
    ]
