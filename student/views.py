from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    return render(request, "landing.html")

def student_home(request):
    return render(request, "student/home.html")