from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from accounts.views import LandingPageView, CalendarView, TimetableView, SyllabusView, FacultyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('student/', include('student.urls', namespace='students')),
    path('faculty/', include('faculty.urls', namespace='faculty')),
    path('classroom/', include('classroom.urls', namespace='classrooms')),
    path('announcement/', include('announcement.urls', namespace='announcements')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('academic-calendar/', CalendarView.as_view(), name='academic-calendar'),
    path('timetable/', TimetableView.as_view(), name='timetable'),
    path('syllabus/', SyllabusView.as_view(), name='syllabus'),
    path('faculty-list/', FacultyView.as_view(), name='faculty-list'),
]


if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)