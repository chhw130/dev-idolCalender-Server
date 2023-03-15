from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.UsersCalendar.as_view()),
    path("<int:pk>", views.UserCalendarDetail.as_view()),
]
