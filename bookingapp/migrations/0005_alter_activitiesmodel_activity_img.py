# Generated by Django 4.2.11 on 2024-04-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookingapp", "0004_alter_activitiesmodel_activity_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activitiesmodel",
            name="activity_img",
            field=models.ImageField(upload_to="bookingapp/static"),
        ),
    ]
