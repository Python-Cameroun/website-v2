# Generated by Django 3.1.4 on 2021-01-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210101_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
