# Generated by Django 4.0.5 on 2022-06-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_projects_githublink_projects_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='githublink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
