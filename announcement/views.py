import django
from django.shortcuts import reverse
from django.views import generic

from .models import Announcement
from .forms import AnnouncementModelForm



class AnnouncementListView(generic.ListView):
    model = Announcement
    template_name = 'announcement/announcement_list.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        return Announcement.objects.all()


class AnnouncementCreateView(generic.CreateView):
    model = Announcement
    template_name = 'announcement/announcement_create.html'
    form_class = AnnouncementModelForm

    def get_success_url(self):
        return reverse('announcement:announcement-list')


class AnnouncementUpdateView(generic.UpdateView):
    template_name = 'announcement/announcement_update.html'
    form_class = AnnouncementModelForm

    def get_success_url(self):
        return reverse('announcement:announcement-list')

    def get_queryset(self):
        return Announcement.objects.all()


class AnnouncementDeleteView(generic.DeleteView):
    template_name = 'announcement/announcement_delete.html'

    def get_success_url(self):
        return reverse('announcement:announcement-list')

    def get_queryset(self):
        return Announcement.objects.all()