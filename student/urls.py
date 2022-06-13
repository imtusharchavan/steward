from django.urls import path

from .views import student_home


app_name = "students"


urlpatterns = [
    path('', student_home),
]