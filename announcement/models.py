from distutils.command.upload import upload
from django.db import models



class Announcement(models.Model):
    title = models.CharField("Title", max_length=50)
    content = models.TextField("Content", null=True, blank=True)
    upload = models.ImageField(null=True, blank=True, upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            '-updated_at',
            '-created_at',
        ]

    def __str__(self):
        return self.title