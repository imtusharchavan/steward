# Generated by Django 4.0.5 on 2022-08-03 12:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_faculty_options_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='designation',
            field=models.CharField(default=datetime.datetime(2022, 8, 3, 12, 52, 24, 235199, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='edu_qualification',
            field=models.CharField(default=datetime.datetime(2022, 8, 3, 12, 52, 46, 932439, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='honors_awards',
            field=models.CharField(default=datetime.datetime(2022, 8, 3, 12, 52, 58, 77271, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='publications',
            field=models.CharField(default=datetime.datetime(2022, 8, 3, 12, 53, 9, 633451, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='research_interests',
            field=models.CharField(default=datetime.datetime(2022, 8, 3, 12, 53, 19, 855784, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='responsibliites',
            field=models.CharField(default=datetime.datetime(2022, 8, 3, 12, 53, 30, 678792, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
