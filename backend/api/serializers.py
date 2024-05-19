from rest_framework import serializers
from .models import IncentiveCalculations, HolidayPackage, User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'user_type', 'token', 'active']

class IncentiveCalculationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = IncentiveCalculations
        fields = ['sales_targets', 'incentive_percentage', 'bonus', 'holiday_package_eligibility' ]

class HolidayPackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HolidayPackage
        fields = [ 'holiday_name', 'durations_nights', 'destination', 'location', 'amenities']

