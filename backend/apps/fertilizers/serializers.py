from rest_framework import serializers
from .models import FertilizerLog

class FertilizerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FertilizerLog
        fields = "__all__"
