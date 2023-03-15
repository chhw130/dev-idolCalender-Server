from django.urls import path
from . import views

urlpatterns = [
    path("", views.Idols.as_view()),  # idol-list  [ GET/  POST ]
    path("<int:pk>", views.IdolDetail.as_view()),  # idol-detail  [GET /  POST, PUT, DELETE]
    path("<int:pk>/schedules", views.IdolSchedule.as_view()),  # only one idol's schedule  [GET / POST]
    path("schedules/", views.Schedules.as_view()),  # all_schedules  [ GET, POST ]
    path("schedules/<int:pk>", views.ScheduleDetail.as_view()),  # #one_schedule  [PUT, DELETE]
]
