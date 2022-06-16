from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from users.mixins import FacultyAndLoginRequiredMixin

from users.models import Classroom
from .forms import ClassroomModelForm



class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class FacultyHomeView(FacultyAndLoginRequiredMixin, generic.TemplateView):
    template_name = "users/faculty.html"


class ClassroomListView(LoginRequiredMixin, generic.ListView):
    template_name = "users/classroom_list.html"
    context_object_name = "classrooms"
   
    def get_queryset(self):
        teacher = self.request.user.userprofile
        return Classroom.objects.filter(teacher=teacher)


class ClassroomDetailView(FacultyAndLoginRequiredMixin, generic.DetailView):
    template_name = "users/classroom_detail.html"
    context_object_name = "classroom"

    def get_queryset(self):
        teacher = self.request.user.userprofile
        return Classroom.objects.filter(teacher=teacher)


class ClassroomCreateView(FacultyAndLoginRequiredMixin, generic.CreateView):
    template_name = "users/classroom_create.html"
    form_class = ClassroomModelForm
    
    def get_success_url(self) :
        return reverse("users:classroom-list")


class ClassroomUpdateView(FacultyAndLoginRequiredMixin, generic.UpdateView):
    template_name = "users/classroom_update.html"
    form_class = ClassroomModelForm
    
    def get_success_url(self) :
        return reverse("users:classroom-list")

    def get_queryset(self):
        teacher = self.request.user.userprofile
        return Classroom.objects.filter(teacher=teacher)


class ClassroomDeleteView(FacultyAndLoginRequiredMixin, generic.DeleteView):
    template_name = "users/classroom_delete.html"

    def get_success_url(self) :
        return reverse("users:classroom-list")
    
    def get_queryset(self):
        teacher = self.request.user.userprofile00
        return Classroom.objects.filter(teacher=teacher)