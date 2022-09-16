from django.contrib import admin

from .models import User, UserProfile, Student, Faculty

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Faculty)