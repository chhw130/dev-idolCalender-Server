
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)

from .models import UserCalendar
from .serializers import UserCalendarSerializer


class UsersCalendar(APIView):
   

    def get(self, request):
        all_calendars = UserCalendar.objects.all()
        serializer = UserCalendarSerializer(
            all_calendars,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCalendarSerializer(data=request.data)
        if serializer.is_valid():
            userCalendar = serializer.save()
            return Response(serializer.data(userCalendar).data)
        else:
            return Response(serializer.errors)


class UserCalendarDetail(APIView):
    

    def get_object(self):
        try:
            return UserCalendar.objects.get(all)
        except UserCalendar.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user_calendar = self.get_object()
        serializer = UserCalendarSerializer(user_calendar)
        return Response(serializer.data)

    def put(self, request, pk):
        user_calendar = self.get_object()
        serializer = UserCalendarSerializer(
            user_calendar,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_user = serializer.save()
            return Response(UserCalendarSerializer(updated_user).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        user_calendar = self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
