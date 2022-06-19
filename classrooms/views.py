from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from users.mixins import FacultyAndLoginRequiredMixin

from users.models import Classroom
from classrooms.forms import ClassroomModelForm


class ClassroomListView(FacultyAndLoginRequiredMixin, generic.ListView):
    template_name = "classrooms/classroom_list.html"
    context_object_name = {
        "classrooms",
        "peoples"
    }
    

    def get_queryset(self):
        peoples = Classroom.people.all()
        user = self.request.user
        # initial queryset of classrooms for particular teacher
        if user.is_faculty:
            queryset = Classroom.objects.filter(department=user.userprofile)
        else:
            queryset = Classroom.objects.filter(people=user.student.classrooms.people)
            # filter for the student that  is logged in
            queryset = queryset.filter(student__user=user)
        return queryset
   
    # def get_queryset(self):
    #     teacher = self.request.user.userprofile
    #     return Classroom.objects.filter(teacher=teacher)


class ClassroomCreateView(FacultyAndLoginRequiredMixin, generic.CreateView):
    template_name = "classrooms/classroom_create.html"
    form_class = ClassroomModelForm
    
    def get_success_url(self) :
        return reverse("classrooms:classroom-list")
    
    def form_valid(self, form):
        classroom = form.save(commit=False)
        classroom.teacher = self.request.user.userprofile
        classroom.save()
        
        return super(ClassroomCreateView, self).form_valid(form)


class ClassroomDetailView(FacultyAndLoginRequiredMixin, generic.DetailView):
    template_name = "classrooms/classroom_detail.html"
    context_object_name = "classroom"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of classrooms for particular teacher
        if user.is_faculty:
            queryset = Classroom.objects.filter(teacher=user.userprofile)
        else:
            queryset = Classroom.objects.filter(teacher=user.student.classrooms.people)
            # filter for the student that  is logged in
            queryset = queryset.filter(student__user=user)
        return queryset

    # def get_queryset(self):
    #     teacher = self.request.user.userprofile
    #     return Classroom.objects.filter(teacher=teacher)


class ClassroomUpdateView(FacultyAndLoginRequiredMixin, generic.UpdateView):
    template_name = "classrooms/classroom_update.html"
    form_class = ClassroomModelForm
    
    def get_success_url(self) :
        return reverse("classrooms:classroom-list")
    
    # def get_queryset(self):
    #     user = self.request.user
    #     return Classroom.objects.filter(teacher=user.userprofile)

    def get_queryset(self):
        teacher = self.request.user.userprofile
        return Classroom.objects.filter(teacher=teacher)


class ClassroomDeleteView(FacultyAndLoginRequiredMixin, generic.DeleteView):
    template_name = "classrooms/classroom_delete.html"

    def get_success_url(self) :
        return reverse("classrooms:classroom-list")

    # def get_queryset(self):
    #     user = self.request.user
    #     return Classroom.objects.filter(teacher=user.userprofile)
    
    def get_queryset(self):
        teacher = self.request.user.userprofile
        return Classroom.objects.filter(teacher=teacher)