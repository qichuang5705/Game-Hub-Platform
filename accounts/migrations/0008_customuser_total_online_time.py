# Generated by Django 5.1.5 on 2025-02-19 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='total_online_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
