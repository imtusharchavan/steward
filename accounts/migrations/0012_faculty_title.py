# Generated by Django 4.0.5 on 2022-08-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_responsibliites_faculty_other_responsibliites'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='title',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Prof.', 'Prof.')], default=1, max_length=6, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
