# Generated by Django 4.0.5 on 2022-07-31 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.course'),
        ),
    ]
