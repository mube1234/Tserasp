from django.forms import models
from rest_framework import serializers
from ..models import Schedule, Driver


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Schedule
        fields='__all__'
