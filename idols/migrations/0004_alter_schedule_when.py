# Generated by Django 4.1.7 on 2023-03-09 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0003_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 12, 59, 5, 804906, tzinfo=datetime.timezone.utc)),
        ),
    ]
