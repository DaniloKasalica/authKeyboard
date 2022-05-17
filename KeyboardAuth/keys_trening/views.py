from django.utils import timezone
from .models import KeyTraining
from .serializers import KeyTrainingSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.views import APIView

class KeyTrainingViewSet(viewsets.ModelViewSet):
    serializer_class = KeyTrainingSerializer
    authentication_classes = ()
    permissions_clases=()

    def get_queryset(self):
        return KeyTraining.objects.filter()
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CustomeKeyTraining(APIView):
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

