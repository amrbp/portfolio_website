# Generated by Django 4.0.5 on 2022-06-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='massage',
            field=models.TextField(blank=True, null=True),
        ),
    ]
