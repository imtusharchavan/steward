# Generated by Django 4.0.5 on 2022-06-13 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_announcement_classroom_delete_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
    ]
