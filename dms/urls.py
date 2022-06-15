from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from users.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPageView.as_view(), name='landing-page'),
    path('users/', include('users.urls', namespace='users')),
    path('classrooms/', include('classrooms.urls', namespace='classrooms')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)