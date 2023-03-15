from django.db import models
from common.models import CommonModel

class Photo(CommonModel):
    title=models.CharField(max_length=150, default="")#사진 제목

    ImgFile = models.URLField()
    
    description = models.CharField(
        max_length=150,
    )

    schedule=models.ForeignKey(#수정 필요 :: 내 일정 업로드시 포토,비디오 가능??
        "usersCalendar.UserCalendar",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    def __str__(self):
        return "Photo File"
    
class Video(CommonModel):
    title=models.CharField(max_length=150, default="")#비디오 제목
    
    VideoFile=models.URLField()

    description=models.CharField(
        max_length=150,
    )    
    schedule=models.ForeignKey(#수정 필요 :: 내 일정 업로드시 포토,비디오 가능??
        "usersCalendar.UserCalendar",
        null=True,
        blank=True,
        on_delete=models.CASCADE,   
        related_name="videos"
    )
    def __str__(self):
        return "Video File"
