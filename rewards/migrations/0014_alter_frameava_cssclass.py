# Generated by Django 5.1.4 on 2025-02-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0013_remove_shop_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frameava',
            name='CssClass',
            field=models.CharField(default='default-ava', max_length=100),
        ),
    ]
