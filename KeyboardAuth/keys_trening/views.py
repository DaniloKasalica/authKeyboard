from django.utils import timezone
from .models import KeyTraining, KeyPairsTraining
from .serializers import KeyPairsTrainingSerializer, KeyTrainingSerializer
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.views import APIView

class KeyTrainingViewSet(viewsets.ModelViewSet):
    serializer_class = KeyTrainingSerializer
   # authentication_classes = (JWTAuthentication)

    filter_fields= ['key', 'user', 'hold_time', 'presure_up', 'presure_down','finger_size_up','finger_size_down','coordinateX_up','coordinateY_up','coordinateX_down','coordinateY_down','date_created','date_edited']
    search_fields = ['^key',  '^hold_time', '^presure_up', '^presure_down','^finger_size_up','^finger_size_down','^coordinateX_up','^coordinateY_up','^coordinateX_down','^coordinateY_down','^date_created','^date_edited']

    ordering_fields = ['key',  'hold_time', 'presure_up', 'presure_down','finger_size_up','finger_size_down','coordinateX_up','coordinateY_up','coordinateX_down','coordinateY_down','date_created','date_edited']
    ordering = ('-date_created')

    def get_queryset(self):
        user = self.request.user
        return KeyTraining.objects.filter(user=user)

    def perform_create(self, serializer):
        print('tuu')
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(account=self.request.user)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        #serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class KeyPairsTrainingViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication)

    serializer_class = KeyPairsTrainingSerializer
    filter_fields= ['keys', 'flight_time', 'hold_time1', 'presure_up1', 'presure_down2','presure_size_up1','presure_size_down2','coordinateX_up1','coordinateY_up1','coordinateX_down2','coordinateY_down2','date_created','date_edited']
    search_fields = ['^keys', 'flight_time','^hold_time1', '^presure_up1', '^presure_down2','^presure_size_up1','^presure_size_down2','^coordinateX_up1','^coordinateY_up1','^coordinateX_down2','^coordinateY_down2','^date_created','^date_edited']
    ordering_fields = ['keys',  'flight_time','hold_time1', 'presure_up1', 'presure_down2','presure_size_up1','presure_size_down2','coordinateX_up1','coordinateY_up1','coordinateX_down2','coordinateY_down2','date_created','date_edited']
    ordering = ('-date_created')

  
    def get_queryset(self):
        user = self.request.user
        return KeyPairsTraining.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



class CreateKeyTraining(APIView):
    def post(self,request):

        payload = request.data

        if not payload:
            return Response({"message": "Sorry for the inconvenience, "
                                        "there has been a problem while creating invoice. "
                                        "Please, contact support.", "data": None,
                             "success": False})


       

      
        for new_item in payload:
            item_obj = {
                "user": request.user.id,
                "key": new_item["key"] if "key" in new_item else None,
                "hold_time": new_item["hold_time"]  if "hold_time" in new_item else None,
                "presure_up": new_item["presure_up"] if "presure_up" in new_item else None,
                "presure_down": new_item["presure_down"]  if "presure_down" in new_item else None,
                "finger_size_up": new_item["finger_size_up"] if "finger_size_up" in new_item else None,
                "finger_size_down": new_item["finger_size_down"]  if "finger_size_down" in new_item else None,
                "coordinateX_up": new_item["coordinateX_up"]  if "coordinateX_up" in new_item else None,
                "coordinateX_down": new_item["coordinateX_down"]  if "coordinateX_down" in new_item else None,
                "coordinateY_down": new_item["coordinateY_down"]  if "coordinateY_down" in new_item else None,
                "coordinateY_up": new_item["coordinateY_up"]  if "coordinateY_up" in new_item else None,
            }
            

            serializer = KeyTrainingSerializer(data=item_obj)

            if not serializer.is_valid(raise_exception=True):
                
                return Response(
                    {"success": False, "message": "Error while trying to create key.", "data": None})

            serializer.save(user=self.request.user)
      

        return Response({"message": "Successfully created keys.", "id": request.user.id, "success": True})

class CreatePairsKeyTraining(APIView):
    def post(self,request):

        payload = request.data

        if not payload:
            return Response({"message": "Sorry for the inconvenience, "
                                        "there has been a problem while creating invoice. "
                                        "Please, contact support.", "data": None,
                             "success": False})


       

      
        for new_item in payload:
            item_obj = {
                "user": request.user.id,
                "keys": new_item["key"] if "key" in new_item else None,
                "flight_time": new_item["flight_time"]  if "flight_time" in new_item else None,
                "hold_time1": new_item["hold_time1"]  if "hold_time1" in new_item else None,
                "presure_up1": new_item["presure_up1"] if "presure_up1" in new_item else None,
                "presure_down2": new_item["presure_down2"]  if "presure_down2" in new_item else None,
                "presure_size_up1": new_item["presure_size_up1"] if "presure_size_up1" in new_item else None,
                "presure_size_down2": new_item["presure_size_down2"]  if "presure_size_down2" in new_item else None,
                "coordinateX_up1": new_item["coordinateX_up1"]  if "coordinateX_up1" in new_item else None,
                "coordinateY_up1": new_item["coordinateY_up1"]  if "coordinateY_up1" in new_item else None,
                "coordinateX_down2": new_item["coordinateX_down2"]  if "coordinateX_down2" in new_item else None,
                "coordinateY_down2": new_item["coordinateY_down2"]  if "coordinateY_down2" in new_item else None,
            }
            

            serializer = KeyPairsTrainingSerializer(data=item_obj)

            if not serializer.is_valid(raise_exception=True):
                
                return Response(
                    {"success": False, "message": "Error while trying to create key.", "data": None})

            serializer.save(user=self.request.user)
      

        return Response({"message": "Successfully created keys.", "id": request.user.id, "success": True})