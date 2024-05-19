from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=15)
    user_type = models.CharField(max_length=25)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username + ':' + self .user_type

class IncentiveCalculations(models.Model):
    sales_targets = models.IntegerField(default=0)
    incentive_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    bonus = models.IntegerField(default=0)
    holiday_package_eligibility = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.sales_targets)
    
class HolidayPackage(models.Model):
    holiday_name = models.CharField(max_length=155)
    durations_nights = models.IntegerField(default=0)
    destination =  models.CharField(max_length=155)
    location = models.CharField(max_length=155)
    amenities = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.holiday_name)
    
