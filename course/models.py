from django.db import models



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