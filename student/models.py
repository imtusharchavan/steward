from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator



class User(AbstractUser):
    fullname = models.CharField("full name", max_length=150)
    is_faculty = models.BooleanField("faculty status", default=False)
    is_student = models.BooleanField("student status", default=False)


def current_year():
        return datetime.date.today().year
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=20, unique=True)
    GENDERS_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDERS_CHOICES)
    date_of_birth = models.DateField()
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING)
    
    def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)
    
    def year_choices():
        return [(r,r) for r in range(1984, datetime.date.today().year+1)]
    
    admission_year = models.IntegerField("admission year", validators=[MinValueValidator(1984), max_value_current_year])

    def __str__(self):
        return self.user.fullname


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.fullname


class Course(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=20)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    faculty = models.ForeignKey("Faculty", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name