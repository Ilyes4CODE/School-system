# Generated by Django 3.2.20 on 2023-08-12 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_student_email_alter_student_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='prof',
        ),
        migrations.RemoveField(
            model_name='module',
            name='student',
        ),
        migrations.AddField(
            model_name='prof',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.module'),
        ),
        migrations.AddField(
            model_name='student',
            name='modules',
            field=models.ManyToManyField(to='dashboard.module'),
        ),
    ]