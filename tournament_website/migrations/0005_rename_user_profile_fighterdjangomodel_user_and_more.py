# Generated by Django 4.1.4 on 2023-01-27 20:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_website', '0004_fighterdjangomodel_delete_fightermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fighterdjangomodel',
            old_name='user_profile',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='fighterdjangomodel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4f30b9a2-58da-4a67-81f1-150ac2d05a74')),
        ),
    ]
