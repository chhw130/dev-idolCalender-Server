# Generated by Django 4.1.7 on 2023-03-12 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0051_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 6, 7, 36, 388773, tzinfo=datetime.timezone.utc)),
        ),
    ]
