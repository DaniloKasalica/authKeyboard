from django.utils import timezone
from .models import TrainingData
from .serializers import TrainingDataSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.views import APIView

class TrainingDataViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingDataSerializer
    authentication_classes = ()
    permissions_clases=()

    def get_queryset(self):
        return TrainingData.objects.filter()
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

class AuthData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """

    OVDJE PROSTOR DA RADIS NESTO SA PODACIMA KOJI SU POSLATI
    DOLJE JE PRIMJER KREIRANJA REDA
        """
        message = ['']
        return Response(message)
    def post(self,request): #POST/GET/PUT

    


        return Response({"message": "Successfully created keys.", "success": True})

