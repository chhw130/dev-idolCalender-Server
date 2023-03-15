from django.urls import path
from . import views


urlpatterns = [
    path("", views.Categories.as_view()),#모든 카테고리에 해당하는 일정 조회, 생성  
    path("<int:pk>", views.CategoryDetail.as_view()), #특정 카테고리에 해당하는 번호의 상세 정보 조회, 수정, 삭제 
]