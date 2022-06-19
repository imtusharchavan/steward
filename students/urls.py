from django.urls import path

from .views import SignupView, StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView


app_name = "students"


urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]