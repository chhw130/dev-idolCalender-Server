# Generated by Django 4.1.7 on 2023-03-10 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0022_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 7, 33, 4, 45444, tzinfo=datetime.timezone.utc)),
        ),
    ]
