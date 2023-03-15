from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,PermissionDenied,ParseError
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Idol, Schedule
from .serializers import IdolsListSerializer, IdolDetailSerializer, ScheduleSerializer

# 난 복제본

class Idols(APIView):#idol-list 

    
    def get(self, request):#조회-> 누구나 가능  (OK)
        all_idols = Idol.objects.all()
        serializer = IdolsListSerializer(all_idols, many=True)
        return Response(serializer.data)

    def post(self, request):  #아이돌 리스트 생성 -> 관리자만 허용  (OK)
        
        if not request.user.is_admin: #관리자 아닌 경우 
            raise PermissionDenied
        serializer = IdolDetailSerializer(data=request.data)
        if serializer.is_valid():# 유효성 체크
            idol = serializer.save()
            return Response(IdolsListSerializer(idol).data)
        
        else:
            return Response(serializer.errors)


class IdolDetail(APIView): #특정 idol-info 
    def get_object(self, pk): 
        try:
            return Idol.objects.get(pk=pk)
        except Idol.DoesNotExist:
            raise NotFound

    def get(self, request, pk): # 조회  (OK)
        idol = self.get_object(pk)
        serializer = IdolDetailSerializer(idol)
        return Response(serializer.data)
    
    def put(self, request, pk): #idol-info 수정 ~> 관리자만 가능 (OK)

        if not request.user.is_admin:
            raise PermissionDenied
        
        idol=self.get_object(pk)
        if request.user.is_admin:
            serializer=IdolDetailSerializer(
                idol,  # user-data
                data=request.data,
                partial=True,
            )

        if serializer.is_valid():
            idol_schedules=request.data.get("idol_schedules")
            if idol_schedules:
                if not isinstance(idol_schedules, list):
                    raise ParseError("Invalid schedules")
                idol.idol_schedules.clear()
                for idol_schedule_pk in idol_schedules: 
                    try:
                        schedule = Idol.objects.get(pk=idol_schedule_pk)
                        idol.idol_schedules.add(schedule)
                    except Schedule.DoesNotExist:
                        raise ParseError("Schedule not Found")
            updated_idol_schedules = serializer.save()
            return Response(IdolDetailSerializer( updated_idol_schedules).data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk): #관리자만 삭제 가능  (OK)
        idol=self.get_object(pk)
        print(request.user.is_admin)
        if request.user.is_admin==False: #관리자가 아닌 경우 
            raise PermissionDenied
        idol.delete()
        if idol.DoesNotExist: #찾는 아이돌이 없는 경우 
            return Response(status=HTTP_204_NO_CONTENT)    

class IdolSchedule(APIView):
    def get_object(self, pk):
        try:
            return Idol.objects.get(pk=pk)
        except Idol.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        idol = self.get_object(pk)
        serializer = ScheduleSerializer(
            idol.idol_schedules.all(),
            many=True,
        )
        return Response(serializer.data)

    
    def post(self, request,pk):#error 수정 필요 
        
        print("post start")
        if not request.user.is_admin:
            raise PermissionDenied
        else:
            idol = self.get_object(pk)
            serializer = ScheduleSerializer(
                data=request.data,
                context={"idol":idol},
            )
            if serializer.is_valid():
                schedule = serializer.save()
                return Response(ScheduleSerializer(schedule).data)
            else:
                return Response(serializer.errors)





class Schedules(APIView): 
    def get(self, request):
        all_schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(all_schedules, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("post start")
        if not request.user.is_admin:
            raise PermissionDenied
        else:
            serializer = ScheduleSerializer(data=request.data)
            if serializer.is_valid():
                schedule = serializer.save()
                return Response(ScheduleSerializer(schedule).data)
            else:
                return Response(serializer.errors)


class ScheduleDetail(APIView):
    def get_object(self, pk):
        try:
            return Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        schedule = self.get_object(pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

    def put(self, request, pk):
        
        if not request.user.is_admin:
            raise PermissionDenied
        
        if request.user.is_admin:
            schedule = self.get_object(pk)
            serializer = ScheduleSerializer(
                schedule,
                data=request.data,
                partial=True,
            )
            if serializer.is_valid():
                updated_schedule = serializer.save()
                return Response(ScheduleSerializer(updated_schedule).data)
            else:
                return Response(serializer.errors)

    def delete(self, request, pk):#(OK)

        schedule = self.get_object(pk)
        if not request.user.is_admin:
            return PermissionDenied
        schedule.delete()
        return Response(status=HTTP_204_NO_CONTENT)