# Generated by Django 4.2.6 on 2023-10-21 10:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_task_feature_alter_feature_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="feature",
            name="executors",
            field=models.ManyToManyField(
                default=[],
                related_name="feature_executors",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]