from django.urls import path
from .views import StudentList, StudentDetail, SectionList, SectionDetail

urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('section/', SectionList.as_view()),
    path('section/<int:pk>/', SectionDetail.as_view()),
    
]