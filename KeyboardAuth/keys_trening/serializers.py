from .models import  TrainingData
from rest_framework import serializers


class TrainingDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingData
        fields = '__all__'
   