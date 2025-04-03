from django.contrib import admin
from  bookingapp import models
# Register your models here.
admin.site.register(models.ActivitiesModel)
admin.site.register(models.BookedActivity)