# Generated by Django 5.1.5 on 2025-02-19 21:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0020_game_views'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='ratting',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Ratting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratting', models.IntegerField()),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='games.game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
