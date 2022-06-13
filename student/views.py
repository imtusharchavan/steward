from django.shortcuts import render
from django.http import HttpResponse

from student.models import Classroom



def landing(request):
    return render(request, "landing.html")


def student_home(request):
    classrooms = Classroom.objects.all()
    context = {
        'classrooms': classrooms
    }
    return render(request, "student/home.html", context)


def classroom(request, pk):
    classroom = Classroom.objects.get(id=pk)
    context = {
        'classroom': classroom
    }
    return render(request, "student/classroom.html", context)
