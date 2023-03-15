from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from common.models import CommonModel
import datetime
# from times.models import TimeModel


class Idol(models.Model):
    """Idol Model Definition"""

    class GroupChoices(models.TextChoices):
        GirlGroup = ("GirlGroup", "GirlGroup")
        BoyGroup = ("BoyGroup", "BoyGroup")

    class SoloChoices(models.TextChoices):
        GirlSolo = ("GirlSolo", "GirlSolo")
        BoySolo = ("BoySolo", "BoySolo")

    class GenderChoices(models.TextChoices):
        Woman = ("Woman", "Woman")
        Man = ("Man", "Man")

    idol_group = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=GroupChoices.choices,
    )
    idol_solo = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=SoloChoices.choices,
    )

    idol_name = models.CharField(max_length=7)
    idol_profile = models.URLField(
        max_length=10000, 
        blank=True, 
        null=True,
        #validators=[URLValidator( "유효한 URL을 입력하세요. ")]
    )

    idol_anniv = models.DateField(default=datetime.date.today)
    idol_birthday = models.DateField()

    idol_gender = models.CharField(
        max_length=5,
        choices=GenderChoices.choices,
    )

    idol_schedules = models.ManyToManyField(
        "idols.Schedule",
        blank=True,
        related_name="idols",
    )

    def str(self):
        return self.idol_name

    class Meta:
        verbose_name_plural = "Our_Idols"


class Schedule(CommonModel):
    """Schedule Model Definition"""

    ScheduleTitle = models.CharField(
        max_length=150,
        default="",
        
    )

    ScheduleType = models.ForeignKey(
        "categories.Category",
        max_length=150,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="schedules",
    )
    location=models.CharField(
        max_length=150,
        default=""
    )
    participant = models.ManyToManyField(
        "idols.Idol",
        max_length=150,
        blank=True,
        related_name="schedules",
    )
    
    ScheduleContent = models.CharField(
        max_length=150,
    )
    when=models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name_plural = "Idol-Schedules"
