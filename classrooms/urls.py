from django.urls import path

from .views import ClassroomListView, ClassroomDetailView, ClassroomCreateView, ClassroomUpdateView, ClassroomDeleteView


app_name = "classrooms"


urlpatterns = [
    path('', ClassroomListView.as_view(), name='classroom-list'),
    path('<int:pk>/', ClassroomDetailView.as_view(), name='classroom-detail'),
    path('<int:pk>/update/', ClassroomUpdateView.as_view(), name='classroom-update'),
    path('<int:pk>/delete/', ClassroomDeleteView.as_view(), name='classroom-delete'),
    path('create/', ClassroomCreateView.as_view(), name='classroom-create'),
]