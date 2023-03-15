from django.db import models
from common.models import CommonModel

# from times.models import TimeModel


class UserCalendar(CommonModel):

    title = models.CharField(max_length=150, default="")  # 일정 제목

    content = models.TextField(max_length=500, default="", blank=True)  # 일정 내용

    owner = models.ForeignKey(  # 일정 주인
        "users.User",
        on_delete=models.CASCADE,
        related_name="usersCalendars",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "User's Calendar"
