from django.urls import path
from .views import StudentSignupView, FacultySignupView, AdminHomeView, StudentHomeView, FacultyHomeView


app_name = "accounts"
 
urlpatterns = [
    path('student-signup/', StudentSignupView.as_view(), name='student-signup'),
    path('faculty-signup/', FacultySignupView.as_view(), name='faculty-signup'),
    path('admin-home/', AdminHomeView.as_view(), name='admin-home'),
    path('student-home/', StudentHomeView.as_view(), name='student-home'),
    path('faculty-home/', FacultyHomeView.as_view(), name='faculty-home'),
]