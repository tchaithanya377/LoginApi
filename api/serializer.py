from rest_framework import serializers
from .models import resister

class register_serializer(serializers.ModelSerializer):
    class Meta:
        model = resister
        fields = ['username', 'email', 'date_joined', 'is_staff', 'is_active', 'password']


