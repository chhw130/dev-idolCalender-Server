from django.db import models


class Category(models.Model):
    class CategoryKindChoices(models.TextChoices):
        BROADCAST = "broadcast", "BROADCASTS"  # 방송
        EVENT = "event", "EVENTS"  # 행사
        RELEASE = "release", "RELEASES"  # 발매
        CONGRAT = "congrats", "CONGRATS"  # 축하
        SNS = "buy", "BUY"  # 구매
        ETC = "etc", "ETC"  # 유저(개인 일정)

    type = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
        default="",
        blank=True,
    )

    content = models.TextField(max_length=500, default="")  # 카테고리에 대한 내용

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Categories"
