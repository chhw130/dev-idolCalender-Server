from django.urls import path
from . import views
urlpatterns = [
    path("", views.Users.as_view()), # 신규가입
    path("userlist", views.AllUsers.as_view()),  # userList[ o ]
    path("admin", views.Admin.as_view()),  # adminProfile (pk:1)

    #path("admin/schedules", views.adminCheckSchedule.as_view()),  # adminScheduele (pk:1)
    
    path("change-password", views.ChangePassword.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),

    
     
    
    path("info/<int:pk>", views.UserDetail.as_view()),
    
    path("reports/", views.AllReport.as_view()),# user가 schedule을 제보
    

    path("login/", views.Login.as_view()),
    path("logout", views.Logout.as_view()),
]