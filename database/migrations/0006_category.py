# Generated by Django 4.0.5 on 2022-06-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_projects_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
