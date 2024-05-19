from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.IncentiveCalculations)
admin.site.register(models.HolidayPackage)
