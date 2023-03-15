# Generated by Django 4.1.7 on 2023-03-12 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_report_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='owner',
            field=models.ForeignKey(default='', max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='report', to=settings.AUTH_USER_MODEL),
        ),
    ]