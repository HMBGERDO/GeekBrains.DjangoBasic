# Generated by Django 3.2.10 on 2022-01-30 12:54

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shopuser",
            name="activation_key",
            field=models.CharField(blank=True, max_length=128, verbose_name="ключ подтверждения"),
        ),
        migrations.AddField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 1, 12, 54, 39, 740536, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
