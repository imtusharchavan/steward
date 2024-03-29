# Generated by Django 4.0.5 on 2022-08-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_faculty_designation_faculty_edu_qualification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='edu_qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='honors_awards',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='publications',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='research_interests',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='responsibliites',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
