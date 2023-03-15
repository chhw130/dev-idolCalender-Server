
from datetime import date
import re

from rest_framework.exceptions import ParseError, ValidationError
from rest_framework import serializers

# 신규 유저 가입 시 확인절차

from .models import User, Report

from idols.models import Idol
from idols.serializers import IdolSerializer 

# 신규 유저 가입 시 확인절차

class TinyUserSerializers(serializers.ModelSerializer):  # simple user-info
    def get_pick(self, user, age):
        request = self.context["request"]
        return Idol.objects.filter(user=request.user, user__pk=user.pk).exists()
    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "nickname",
            "age",
            "email",
            "profileImg",
            "pick",
        )
class PrivateUserSerializer(serializers.ModelSerializer):# 회원가입시 이용하는 serial
    # pick = IdolsListSerializer()
    class Meta:
        model = User
        exclude = (
            #"password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "last_login",
            "name",
            "is_admin",
        )
    def validate_age(self, age):
        print("check age")
        if age:
            if age<=14 and age>=0:
                raise ParseError("15세 부터 가입 가능합니다.")
            
        else: raise ParseError("나이를 입력해 주세요.")
        return age 
    
    def validate_password(self, password):
        if not re.search(r'[a-z]', password):
            raise ValidationError("비밀번호는 영문 소문자를 포함해야 합니다.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("비밀번호는 영문 대문자를 포함해야 합니다.")
        if not re.search(r'[0-9]', password):
            raise ValidationError("비밀번호는 숫자를 포함해야 합니다.")
        if not re.search(r'[~!@#$%^&*()_+{}":;\']', password):
            raise ValidationError("비밀번호는 특수문자(~!@#$%^&*()_+{}\":;\')를 포함해야 합니다.")
        if len(password) < 8 or len(password) > 16:
            raise ValidationError("비밀번호는 8자 이상 16자 이하이어야 합니다.")
        else:  return password

                
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "first_name",
            "last_name",
            "name",
            "age",
            "is_superuser",
            "is_admin",
            "is_staff",
            "user_permissions"
        )


class ReportSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Report
        fields="__all__"


class ReportDetailSerializer(serializers.ModelSerializer):
    owner=TinyUserSerializers(read_only=True) #작성자
    whoes=IdolSerializer(many=True, read_only=True)#참여자
    class Meta:
        model=Report
        fields="__all__"


    def validate_whoes(self, value):
        
        if not value:
            raise ParseError("제보 대상을 알려 주세요")
        if not isinstance(value, list):
            if value:
                raise ParseError("who_pk must be a list")
            else:
                raise ParseError("whoes report? Who should be required. not null")
            
        # if not value:
        #     raise serializers.ValidationError("참여자를 선택해주세요.")
        # for idol in value:
        #     if idol.pick != self.context['request'].user.pick:
        #         raise serializers.ValidationError("참여자는 본인의 아이돌만 선택 가능합니다.")
        return value
    
    
