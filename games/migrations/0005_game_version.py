# Generated by Django 5.1.4 on 2025-01-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='version',
            field=models.TextField(default=1.0, max_length=15),
        ),
    ]
