# Generated by Django 5.1.5 on 2025-01-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_genre_remove_game_genre_game_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, default='media', upload_to='image/'),
        ),
    ]
