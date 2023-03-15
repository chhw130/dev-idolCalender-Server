from django.db import models


class TimeModel(models.Model):

    start_time = models.DateTimeField(null=True, blank=False)
    end_time = models.DateTimeField(null=True, blank=True)
