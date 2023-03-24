# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("rest_email_auth", "0002_emailconfirmation")]

    operations = [
        migrations.AlterField(
            model_name="emailaddress",
            name="email",
            field=models.EmailField(
                max_length=255, unique=True, verbose_name="email"
            ),
        )
    ]
