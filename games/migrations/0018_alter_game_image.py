# Generated by Django 5.1.4 on 2025-02-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0017_alter_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='games/image'),
        ),
    ]
