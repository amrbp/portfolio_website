# Generated by Django 4.0.5 on 2022-06-11 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.CharField(choices=[('frontend', 'frontend'), ('website', 'website'), ('ux/ui', 'ux/ui')], default=1, max_length=8),
            preserve_default=False,
        ),
    ]
