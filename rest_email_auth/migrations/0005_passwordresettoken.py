# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-05 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [("rest_email_auth", "0004_emailaddress_is_primary")]

    operations = [
        migrations.CreateModel(
            name="PasswordResetToken",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The time at which the password reset token was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "key",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="The token that authorizes the user to reset their password.",
                        verbose_name="key",
                    ),
                ),
                (
                    "email",
                    models.ForeignKey(
                        editable=False,
                        help_text="The email address used to request the password reset.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="password_reset_tokens",
                        related_query_name="password_reset_token",
                        to="rest_email_auth.EmailAddress",
                        verbose_name="email address",
                    ),
                ),
            ],
            options={
                "verbose_name": "password reset token",
                "verbose_name_plural": "password reset tokens",
            },
        )
    ]
