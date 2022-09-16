# Generated by Django 4.0.5 on 2022-08-03 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_faculty_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.semester'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='title',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Prof.', 'Prof.')], default='1', max_length=6, verbose_name='Title'),
        ),
    ]