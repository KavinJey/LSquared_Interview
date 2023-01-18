import os, glob
import json

from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import DeviceModel, ContentEventModel
from .serializers import DeviceSerializer


class DevicesListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (AllowAny,)
    paginator = None


class ImageListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        """
        Return list of images in /content/assets
        with name, size, type
        """
        print(os.getcwd())
        asset_path = f"{os.getcwd()}/lsquared/content/assets"
        assets = os.listdir(asset_path)
        images = []
        for image_name in assets:
            with open(os.path.join(asset_path, image_name), "r") as image:
                image_size = image.seek(0, os.SEEK_END)
                images.append({"size": image_size, "name": image_name, "type": "image"})

        return Response(images)


class ContentEventCreateView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        Creates JSON for every device
        as well as creates ContentEvent model
        to db

        { devices { [DeviceModel] }
          content { [Images]}
          st time
          et time
        }
        """

        payload = request.data
        devices_list = payload["devices"]
        content_list = payload["content"]
        json_folder_path = f"{os.getcwd()}/lsquared/content/json"
        for device in devices_list:
            for content in content_list:
                content_event = ContentEventModel.objects.create(
                    device_id=device["id"],
                    content_name=content["name"],
                    content_type=content["type"],
                    content_size=content["size"],
                    start_time=payload["st"],
                    end_time=payload["et"],
                )

                json_file_path = f'{json_folder_path}/{device["name"]}.json'
                file_exists = os.path.isfile(json_file_path)
                if file_exists:
                    with open(json_file_path, "r+") as json_file:
                        content_json = json.load(json_file)
                        content_json["content"].append(
                            {
                                "id": content_event.id,
                                "type": content_event.content_type,
                                "fileSize": content_event.content_size,
                                "fileName": content_event.content_name,
                                "st": content_event.start_time,
                                "et": content_event.end_time,
                            }
                        )
                        json_file.write(json.dumps(content_json))

                        print(content_json)

                    json_file.close()

                else:
                    with open(json_file_path, "x") as json_file:
                        content_json = {
                            "device": {
                                "info": {"id": device["id"], "name": device["name"]}
                            },
                            "content": [
                                {
                                    "id": content_event.id,
                                    "type": content_event.content_type,
                                    "fileSize": content_event.content_size,
                                    "fileName": content_event.content_name,
                                    "st": content_event.start_time,
                                    "et": content_event.end_time,
                                }
                            ],
                        }
                        json_file.write(json.dumps(content_json))
                    json_file.close()

        print(payload)

        # Save data to table with
        # id, deviceid, content_+name, content_type
        # content_size, start_time, end_time

        # create json for each device in payload
        # if user submits post for device that already has content, add content to json

        content = ContentEventModel.objects.all()

        return Response(status=201)
