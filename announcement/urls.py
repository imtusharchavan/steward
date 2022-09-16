from django.urls import path

from .views import AnnouncementListView, AnnouncementCreateView, AnnouncementUpdateView, AnnouncementDeleteView


app_name = "announcement"


urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement-list'),
    path('create/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement-delete'),
]