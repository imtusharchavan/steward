from django.urls import path

from .views import FacultyHomeView


app_name = "users"


urlpatterns = [
    path('', FacultyHomeView.as_view(), name='faculty'),
    # path('student/', StudentHomeView.as_view(), name='student'),
]