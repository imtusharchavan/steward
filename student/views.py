from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Semester


def landing(request):
    return render(request, "landing.html")

def student_home(request):
    return render(request, "students/home.html")