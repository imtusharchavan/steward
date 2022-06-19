from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# from .views import FacultyHomeView, ClassroomListView, ClassroomDetailView, ClassroomCreateView, ClassroomUpdateView, ClassroomDeleteView


app_name = "users"
 
urlpatterns = [
    # path('classrooms/', ClassroomListView.as_view(), name='classroom-list'),
    # path('classrooms/<int:pk>/', ClassroomDetailView.as_view(), name='classroom-detail'),
    # path('classrooms/<int:pk>/update/', ClassroomUpdateView.as_view(), name='classroom-update'),
    # path('classrooms/<int:pk>/delete/', ClassroomDeleteView.as_view(), name='classroom-delete'),
    # path('classrooms/create/', ClassroomCreateView.as_view(), name='classroom-create'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]