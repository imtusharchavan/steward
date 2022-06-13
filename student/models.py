from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_faculty = models.BooleanField("faculty status", default=False)
    is_student = models.BooleanField("student status", default=False)
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_no = models.CharField("Enrollment No", max_length=20, unique=True)
    GENDERS_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField("Gender", max_length=1, choices=GENDERS_CHOICES)
    date_of_birth = models.DateField("Date of birth")
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING)
    YEAR_CHOICES = [
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Final')
    ]
    current_year = models.CharField("Current year", max_length=1, choices=YEAR_CHOICES, default='1')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Course(models.Model):
    code = models.CharField("Course code", max_length=20, unique=True)
    name = models.CharField("Course name", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    semester = models.CharField("Semester", max_length=20)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.semester


class Subject(models.Model):
    code = models.CharField("Subject code", max_length=20, unique=True)
    name = models.CharField("Subject name", max_length=50)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    code = models.CharField("Class code", max_length=50, unique=True)
    name = models.CharField("Class name", max_length=50)
    subject = models.ForeignKey("Subject", on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey("Faculty", null=True, blank=True, on_delete=models.SET_NULL)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    # people = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Stream(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    classroom = models.ForeignKey("Classroom", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]