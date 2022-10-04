
from rest_framework import serializers
from .models import Maestro, Salon

class MaestroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Maestro
        fields="__all__"

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Salon
        fields="__all__"