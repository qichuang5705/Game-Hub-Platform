# Generated by Django 5.1.3 on 2025-02-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadAssset', '0002_alter_asset_thumnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='thumnail',
            field=models.ImageField(blank=True, default='defaults/NoneImage.png', null=True, upload_to='thumnail/%Y/%m'),
        ),
    ]
