# Generated by Django 5.1.5 on 2025-02-19 12:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FrameAvatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=100)),
                ('image', models.ImageField(default='default/gojo.jpg', upload_to='rewards/')),
                ('CssClass', models.TextField(default='default-avatar', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FrameChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=100)),
                ('image', models.ImageField(default='default/gojo.jpg', upload_to='rewards/')),
                ('CssClass', models.TextField(default='default-chat', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatar_class', to=settings.AUTH_USER_MODEL)),
                ('frame_avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewards.frameavatar')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_class', to=settings.AUTH_USER_MODEL)),
                ('frame_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewards.framechat')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewards.avatar')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewards.chat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
