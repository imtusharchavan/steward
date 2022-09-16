from django.shortcuts import reverse
from django.views import generic
from accounts.mixins import FacultyAndLoginRequiredMixin

from .models import Classroom
from .forms import ClassroomModelForm


class ClassroomListView(FacultyAndLoginRequiredMixin, generic.ListView):
    template_name = "classrooms/classroom_list.html"
    context_object_name = "classrooms"
    

    def get_queryset(self):
        user = self.request.user
        # initial queryset of classrooms for particular teacher
        if user.is_faculty:
            queryset = Classroom.objects.filter(teacher=user.userprofile)
        else:
            queryset = Classroom.objects.filter(teacher=user.faculty.department)
            # filter for the student that  is logged in
            queryset = queryset.filter(student__user=user)
        return queryset
   
    # def get_queryset(self):
    #     teacher = self.request.user.userprofile
    #     return Classroom.objects.filter(teacher=teacher)


class ClassroomCreateView(FacultyAndLoginRequiredMixin, generic.CreateView):
    template_name = "classroom/classroom_create.html"
    form_class = ClassroomModelForm
    
    def get_success_url(self) :
        return reverse("classroom:classroom-list")
    
    def form_valid(self, form):
        classrooms = form.save(commit=False)
        classrooms.teacher = self.request.user.userprofile
        classrooms.save()
        
        return super(ClassroomCreateView, self).form_valid(form)


class ClassroomDetailView(FacultyAndLoginRequiredMixin, generic.DetailView):
    template_name = "classroom/classroom_detail.html"
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
    template_name = "classroom/classroom_update.html"
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
    template_name = "classroom/classroom_delete.html"

    def get_success_url(self) :
        return reverse("classroom:classroom-list")

    # def get_queryset(self):
    #     user = self.request.user
    #     return Classroom.objects.filter(teacher=user.userprofile)
    
    def get_queryset(self):
        teacher = self.request.user.userprofile
        return Classroom.objects.filter(teacher=teacher)