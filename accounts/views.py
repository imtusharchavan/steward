from accounts.mixins import StudentAndAdminLoginRequiredMixin, FacultyAndAdminLoginRequiredMixin, FacultyAndLoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views import generic

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import CustomUserCreationForm
from .models import Faculty


# def login_view(request):
#     next = request.GET.get('next')
#     form = CustomUserCreationForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if next:
#             if user != None:
#                 login(request, user)
#                 if  user.is_staff:
#                     return redirect(reverse('accounts:admin_home'))
#                 elif user.is_student:
#                     return redirect(reverse('accounts:student_home'))
#                 elif user.is_faculty:
#                     return redirect(reverse('accounts:faculty_home'))
#             return redirect("/")
        
        


#     context = {
#         'form': form,
#     }
#     return render(request, "login.html", context)


class StudentSignupView(StudentAndAdminLoginRequiredMixin, generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) :
        return reverse("students:student-create")


class FacultySignupView(FacultyAndAdminLoginRequiredMixin, generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) :
        return reverse("faculty:faculty-create")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class CalendarView(generic.TemplateView):
    template_name = "academics/calendar.html"


class TimetableView(generic.TemplateView):
    template_name = "academics/timetable.html"


class SyllabusView(generic.TemplateView):
    template_name = "academics/syllabus.html"


class FacultyView(generic.ListView):
    template_name = "faculty_mainlist.html"
    context_object_name = "faculty"

    def get_queryset(self):
        return Faculty.objects.all()


class AdminHomeView(generic.TemplateView):
    template_name = "accounts/admin_home.html"

    
class StudentHomeView(generic.TemplateView):
    template_name = "accounts/student_home.html"


class FacultyHomeView(FacultyAndLoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/faculty_home.html"