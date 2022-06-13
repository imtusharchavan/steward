from django.urls import path

from .views import student_home, classroom


app_name = "student"


urlpatterns = [
    path('', student_home),
    path('classrooms/<pk>/', classroom)
]