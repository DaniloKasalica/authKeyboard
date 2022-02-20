from .models import KeyTraining, KeyPairsTraining
from rest_framework.relations import PrimaryKeyRelatedField

from rest_framework import serializers


class KeyPairsTrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyPairsTraining
        fields = ('keys', 'flight_time', 'hold_time1', 'presure_up1', 'presure_down2','presure_size_up1','presure_size_down2','coordinateX_up1','coordinateY_up1','coordinateX_down2','coordinateY_down2','date_created','date_edited','user')

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(KeyPairsTrainingSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
class KeyTrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyTraining
        fields = ('key',  'hold_time', 'presure_up', 'presure_down','finger_size_up','finger_size_down','coordinateX_up','coordinateY_up','coordinateY_down','coordinateX_down','date_created','date_edited','user')

    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)
        super(KeyTrainingSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
