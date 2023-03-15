from django.db import models


class CommonModel(models.Model):
    """CommonModel Definition"""

    created_at = models.DateTimeField(  # 생성일시
        null=True,
        auto_now_add=True,
    )  # 처음 생성시
    updated_at = models.DateTimeField(  # 종료일시
        null=True,
        auto_now=True,
    )  # 업데이트 할때 마다

    class Meta:  # db에 넣지마
        abstract = True
