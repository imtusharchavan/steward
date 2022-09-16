from django.shortcuts import reverse
from django.views import generic
from accounts.mixins import FacultyAndAdminLoginRequiredMixin

from accounts.models import Faculty
from .forms import FacultyModelForm



class FacultyListView(FacultyAndAdminLoginRequiredMixin, generic.ListView):
    template_name = "faculty/faculty_list.html"
    context_object_name = "faculty"
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Faculty.objects.filter(department=department)


class FacultyCreateView(FacultyAndAdminLoginRequiredMixin, generic.CreateView):
    template_name = "faculty/faculty_create.html"
    form_class = FacultyModelForm
    
    def get_success_url(self) :
        return reverse("faculty:faculty-list")
    
    def form_valid(self, form):
        faculty = form.save(commit=False)
        faculty.department = self.request.user.userprofile
        faculty.save()
        return super(FacultyCreateView, self).form_valid(form)


class FacultyDetailView(FacultyAndAdminLoginRequiredMixin, generic.DetailView):
    template_name = "faculty/faculty_detail.html"
    context_object_name = "faculty"

    def get_queryset(self):
        department = self.request.user.userprofile
        return Faculty.objects.filter(department=department)


class FacultyUpdateView(FacultyAndAdminLoginRequiredMixin, generic.UpdateView):
    template_name = "faculty/faculty_update.html"
    form_class = FacultyModelForm
    
    def get_success_url(self) :
        return reverse("faculty:faculty-list")
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Faculty.objects.filter(department=department)


class FacultyDeleteView(FacultyAndAdminLoginRequiredMixin, generic.DeleteView):
    template_name = "faculty/faculty_delete.html"
    
    def get_success_url(self) :
        return reverse("faculty:faculty-list")
    
    def get_queryset(self):
        department = self.request.user.userprofile
        return Faculty.objects.filter(department=department)