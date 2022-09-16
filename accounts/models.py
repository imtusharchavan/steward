from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from course.models import Course, Semester



class User(AbstractUser):
    is_faculty = models.BooleanField("faculty status", default=False)
    is_student = models.BooleanField("student status", default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    GENDERS_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField("Gender", max_length=6, choices=GENDERS_CHOICES)
    date_of_birth = models.DateField("Date of birth")
    phone_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=1)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    YEAR_CHOICES = [
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Final')
    ]
    current_year = models.CharField("Current year", max_length=1, choices=YEAR_CHOICES, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")
    phone_number = models.CharField(max_length=20)
    TITLE_CHOICES = [
        ('Dr.', 'Dr.'),
        ('Prof.', 'Prof.'),
    ]
    title = models.CharField("Title", max_length=6, choices=TITLE_CHOICES, default='1')
    designation = models.CharField(null=True, blank=True, max_length=100)
    educational_qualification = models.CharField(null=True, blank=True, max_length=100)
    honors_awards = models.CharField(null=True, blank=True, max_length=200)
    research_interests = models.CharField(null=True, blank=True, max_length=200)
    publications = models.CharField(null=True, blank=True, max_length=200)
    other_responsibliites = models.CharField(null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)