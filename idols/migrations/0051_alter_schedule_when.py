# Generated by Django 4.1.7 on 2023-03-12 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0050_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 5, 45, 38, 483140, tzinfo=datetime.timezone.utc)),
        ),
    ]