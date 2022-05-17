from .models import  KeyTraining
from rest_framework import serializers


class KeyTrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyTraining
        fields = '__all__'
   