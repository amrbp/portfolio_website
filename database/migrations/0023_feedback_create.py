# Generated by Django 4.0.5 on 2022-06-16 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0022_remove_projects_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
