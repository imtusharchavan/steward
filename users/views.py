# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# from .models import Classroom




class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class FacultyHomeView(generic.TemplateView):
    template_name = "users/faculty.html"


class StudentHomeView(generic.TemplateView):
    template_name = "users/student.html"