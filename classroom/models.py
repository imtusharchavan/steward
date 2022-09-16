from django.db import models

from accounts.models import User, UserProfile
from course.models import Subject



class Classroom(models.Model):
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    code = models.CharField("Class code", max_length=50, unique=True)
    name = models.CharField("Class name", max_length=50)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)
    people = models.ManyToManyField(User, related_name='people', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name