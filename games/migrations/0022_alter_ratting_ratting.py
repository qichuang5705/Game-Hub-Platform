# Generated by Django 5.1.5 on 2025-02-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0021_game_ratting_ratting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratting',
            name='ratting',
            field=models.IntegerField(default=0),
        ),
    ]
