# Generated by Django 5.1.4 on 2025-02-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_project_live_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='archivelink',
            field=models.URLField(blank=True),
        ),
    ]
