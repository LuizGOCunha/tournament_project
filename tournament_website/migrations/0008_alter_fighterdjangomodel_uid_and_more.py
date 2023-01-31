# Generated by Django 4.1.4 on 2023-01-30 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament_website', '0007_alter_fighterdjangomodel_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighterdjangomodel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('c1f06949-6d75-4744-b8c3-880fbfa3eae9')),
        ),
        migrations.AlterField(
            model_name='fighterdjangomodel',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fighter', to=settings.AUTH_USER_MODEL),
        ),
    ]