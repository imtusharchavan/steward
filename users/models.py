from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField("admin status", default=False)
    is_faculty = models.BooleanField("faculty status", default=False)
    is_student = models.BooleanField("student status", default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    enrollment_no = models.CharField("Enrollment No", max_length=20, unique=True)
    GENDERS_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField("Gender", max_length=6, choices=GENDERS_CHOICES)
    date_of_birth = models.DateField("Date of birth")
    phone_number = models.CharField(max_length=20)
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
    teacher = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    code = models.CharField("Class code", max_length=50, unique=True)
    name = models.CharField("Class name", max_length=50)
    subject = models.ForeignKey("Subject", null=True, blank=True, on_delete=models.SET_NULL)
    # students = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = [
            '-updated_at',
            '-created_at',
        ]

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    classroom = models.ForeignKey("Classroom", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)