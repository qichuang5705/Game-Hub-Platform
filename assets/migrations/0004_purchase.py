# Generated by Django 5.1.3 on 2025-02-10 16:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_alter_asset_thumnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')], max_length=50)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.asset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
