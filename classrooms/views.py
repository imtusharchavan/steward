# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import generic
# from users.mixins import FacultyAndLoginRequiredMixin

# from users.models import Classroom
# from .forms import ClassroomModelForm



# class ClassroomListView(LoginRequiredMixin, generic.ListView):
#     template_name = "classrooms/classroom_list.html"
   
#     def get_queryset(self):
#         teacher = self.request.user.userprofile
#         return Classroom.objects.filter(teacher=teacher)
#     context_object_name = "classrooms"


# class ClassroomDetailView(FacultyAndLoginRequiredMixin, generic.DetailView):
#     template_name = "classrooms/classroom_detail.html"

#     def get_queryset(self):
#         teacher = self.request.user.userprofile
#         return Classroom.objects.filter(teacher=teacher)
#     context_object_name = "classroom"


# class ClassroomCreateView(FacultyAndLoginRequiredMixin, generic.CreateView):
#     template_name = "classrooms/classroom_create.html"
#     form_class = ClassroomModelForm
    
#     def get_success_url(self) :
#         return reverse("classrooms:classroom-list")


# class ClassroomUpdateView(FacultyAndLoginRequiredMixin, generic.UpdateView):
#     template_name = "classrooms/classroom_update.html"
#     form_class = ClassroomModelForm
    
#     def get_success_url(self) :
#         return reverse("classrooms:classroom-list")

#     def get_queryset(self):
#         teacher = self.request.user.userprofile
#         return Classroom.objects.filter(teacher=teacher)


# class ClassroomDeleteView(FacultyAndLoginRequiredMixin, generic.DeleteView):
#     template_name = "classrooms/classroom_delete.html"

#     def get_success_url(self) :
#         return reverse("classrooms:classroom-list")
    
#     def get_queryset(self):
#         teacher = self.request.user.userprofile00
#         return Classroom.objects.filter(teacher=teacher)