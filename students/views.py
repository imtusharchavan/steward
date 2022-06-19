from django.core.mail import send_mail
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from users.mixins import AdminAndLoginRequiredMixin

from users.models import Student
from .forms import StudentModelForm, CustomUserCreationForm



class SignupView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) :
        return reverse("students:student-create")


class StudentListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "students/student_list.html"
    context_object_name = "students"
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)


class StudentCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name = "students/student_create.html"
    form_class = StudentModelForm
    
    def get_success_url(self) :
        return reverse("students:student-list")
    
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


class StudentDetailView(AdminAndLoginRequiredMixin, generic.DetailView):
    template_name = "students/student_detail.html"
    context_object_name = "student"

    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)


class StudentUpdateView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_update.html"
    form_class = StudentModelForm
    
    def get_success_url(self) :
        return reverse("students:student-list")
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)


class StudentDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "students/student_delete.html"
    
    def get_success_url(self) :
        return reverse("students:student-list")
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Student.objects.filter(department=department)