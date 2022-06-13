from django.contrib import admin
from django.urls import path, include
from student.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", landing),
    path('student/', include('student.urls', namespace='student')),
]