# Generated by Django 5.0.1 on 2024-01-27 13:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "facultyDataManager",
            "0007_rename_name_of_the_faculty_guestlecture_name_of_the_guest_lecture_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="conferencechair",
            name="name_of_the_conference",
        ),
    ]
