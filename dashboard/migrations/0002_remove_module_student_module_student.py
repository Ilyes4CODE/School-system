# Generated by Django 4.2.2 on 2023-07-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='student',
        ),
        migrations.AddField(
            model_name='module',
            name='student',
            field=models.ManyToManyField(to='dashboard.student'),
        ),
    ]
