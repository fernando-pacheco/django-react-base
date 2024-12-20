from rest_framework import serializers
from .models import BaseIntModel, BaseUUIDModel


class BaseIntSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseIntModel
        fields = '__all__'


class BaseUUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUUIDModel
        fields = '__all__'
