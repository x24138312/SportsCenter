# Generated by Django 4.2.11 on 2024-04-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookingapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookedactivity",
            old_name="end_time",
            new_name="date_of_booking",
        ),
        migrations.RemoveField(
            model_name="bookedactivity",
            name="start_time",
        ),
        migrations.AddField(
            model_name="bookedactivity",
            name="activity_slot",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="activitiesmodel",
            name="activity_img",
            field=models.ImageField(upload_to="static"),
        ),
    ]
