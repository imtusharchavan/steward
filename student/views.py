from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views import generic
from accounts.mixins import StudentAndAdminLoginRequiredMixin

from accounts.models import Student
from .forms import StudentModelForm


class StudentListView(StudentAndAdminLoginRequiredMixin, generic.ListView):
    template_name = "student/student_list.html"
    context_object_name = "students"
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)


class StudentCreateView(StudentAndAdminLoginRequiredMixin, generic.CreateView):
    template_name = "student/student_create.html"
    form_class = StudentModelForm
    
    def get_success_url(self) :
        return reverse("student:student-list")
    
    def form_valid(self, form):
        student = form.save(commit=False)
        student.department = self.request.user.userprofile
        student.save()
        send_mail(
            subject="Your student account has been created at DBATU (IT)",
            message="Please change your password and login to the portal by clicking on this link..",
            from_email="it@dbatu.ac.in",
            recipient_list=["student@gmail.com"]
        )
        return super(StudentCreateView, self).form_valid(form)


class StudentDetailView(StudentAndAdminLoginRequiredMixin, generic.DetailView):
    template_name = "student/student_detail.html"
    context_object_name = "student"

    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)


class StudentUpdateView(StudentAndAdminLoginRequiredMixin, generic.UpdateView):
    template_name = "student/student_update.html"
    form_class = StudentModelForm
    
    def get_success_url(self) :
        return reverse("student:student-list")
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)


class StudentDeleteView(StudentAndAdminLoginRequiredMixin, generic.DeleteView):
    template_name = "student/student_delete.html"
    
    def get_success_url(self) :
        return reverse("student:student-list")
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)