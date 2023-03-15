
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from .models import Idol, Schedule
from categories.serializers import CategorySerializer

class IdolsListSerializer(ModelSerializer):
    class Meta:
        model = Idol
        fields = ("pk", "idol_name", "idol_group","idol_solo", "idol_profile", )


class ScheduleSerializer(ModelSerializer):
    ScheduleType = CategorySerializer(read_only=True)
    participant = IdolsListSerializer(many=True, read_only=True)
    
    when=serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Schedule
        fields = (
            "pk",
            
            "ScheduleTitle",
            "ScheduleType",
            "location",
            "when",
            "ScheduleContent",
            "participant",
        )

        


class IdolDetailSerializer(ModelSerializer):
    
    idol_schedules = ScheduleSerializer(
        read_only=True, many=True  # 스케줄을 필수 항목으로 인식하지 않음
    )

    class Meta:
        model = Idol
        fields = "__all__"
    
    def validate(self, attrs):
        idol_gender=attrs.get('idol_gender')
        idol_solo=attrs.get('idol_solo')
        idol_group=attrs.get('idol_group')

        if idol_gender=="Man":
            if idol_solo=="GirlSolo" or idol_group=="GirlGroup":
                raise ParseError("남자인 아이돌은 여성 항목을 선택할 수 없습니다.")
        else:
            if idol_solo=="BoySolo" or idol_group=="BoyGroup":
                raise ParseError("여자인 아이돌은 남성 항목을 선택할 수 없습니다.")
        return attrs    


    








class IdolSerializer(ModelSerializer):
    class Meta:
        model=Idol
        fields=("idol_name",)
            
