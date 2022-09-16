from django.urls import path

from .views import FacultyListView, FacultyCreateView, FacultyDetailView, FacultyUpdateView, FacultyDeleteView


app_name = "faculty"


urlpatterns = [
    path('', FacultyListView.as_view(), name='faculty-list'),
    path('create/', FacultyCreateView.as_view(), name='faculty-create'),
    path('<int:pk>/', FacultyDetailView.as_view(), name='faculty-detail'),
    path('<int:pk>/update/', FacultyUpdateView.as_view(), name='faculty-update'),
    path('<int:pk>/delete/', FacultyDeleteView.as_view(), name='faculty-delete'),
]