from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from student.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPageView.as_view(), name='landing-page'),
    path('student/', include('student.urls', namespace='student')),
]


if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)