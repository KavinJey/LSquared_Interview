import os, glob 

from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import DeviceModel, ContentEventModel
from .serializers import DeviceSerializer

class DevicesListView(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
  queryset = DeviceModel.objects.all()
  serializer_class = DeviceSerializer
  permission_classes = (AllowAny, )
  paginator = None



class ImageListView(views.APIView):
  permission_classes = (AllowAny, )

  def get(self, request):
    """
    Return list of images in /content/assets 
    with name, size, type
    """
    print(os.getcwd())
    asset_path = f'{os.getcwd()}/lsquared/content/assets'
    assets = os.listdir(asset_path)
    images = []
    for image_name in assets:
      with open(os.path.join(asset_path, image_name), 'r') as image:
        image_size = image.seek(0, os.SEEK_END)
        images.append({"size": image_size, "name": image_name, "type": 'image' })

    return Response(images)

  

class ContentEventCreateView(views.APIView):
  permission_classes = (AllowAny, )
  
  def post(self, request):
    """
    Creates JSON for every device
    as well as creates ContentEvent model
    to db 
    """
    content = ContentEventModel.objects.all()

    return Response(content)