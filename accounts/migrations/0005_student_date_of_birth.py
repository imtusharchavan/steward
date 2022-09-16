# Generated by Django 4.0.5 on 2022-08-02 15:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 8, 2, 15, 33, 1, 903691, tzinfo=utc), verbose_name='Date of birth'),
            preserve_default=False,
        ),
    ]
