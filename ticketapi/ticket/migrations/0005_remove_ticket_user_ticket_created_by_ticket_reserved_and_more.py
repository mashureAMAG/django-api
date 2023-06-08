# Generated by Django 4.2.1 on 2023-06-07 14:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ticket", "0004_alter_ticket_validity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="user",
        ),
        migrations.AddField(
            model_name="ticket",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="reserved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ticket",
            name="reserved_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reserved_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="validity",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 14, 14, 39, 2, 885773)
            ),
        ),
    ]
