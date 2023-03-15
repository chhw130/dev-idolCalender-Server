from rest_framework.serializers import ModelSerializer
from .models import UserCalendar


class UserCalendarSerializer(ModelSerializer):
    class Meta:
        model = UserCalendar
        fields = (
            "pk",
            "owner",
            "title",
            "content",
            # "start_date", // 필요
            # "end_date", // 필요
        )
