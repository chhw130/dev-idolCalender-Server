# Generated by Django 4.1.7 on 2023-03-13 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0067_rename_description_schedule_schedulecontent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idol',
            name='idol_name',
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 13, 5, 36, 47, 294296, tzinfo=datetime.timezone.utc)),
        ),
    ]