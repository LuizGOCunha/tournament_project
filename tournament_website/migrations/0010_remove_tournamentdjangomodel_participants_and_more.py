# Generated by Django 4.1.4 on 2023-02-10 19:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        (
            "tournament_website",
            "0009_alter_fighterdjangomodel_uid_tournamentdjangomodel",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tournamentdjangomodel",
            name="participants",
        ),
        migrations.AddField(
            model_name="fighterdjangomodel",
            name="tournament",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="participant",
                to="tournament_website.tournamentdjangomodel",
            ),
        ),
        migrations.AlterField(
            model_name="fighterdjangomodel",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("4384126c-d058-4e05-a826-8cc5a4ec1b57")
            ),
        ),
    ]
