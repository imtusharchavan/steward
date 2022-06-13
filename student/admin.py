from django.contrib import admin

from student.models import User, Student, Faculty, Course, Semester,Subject, Classroom, Stream

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(Stream)