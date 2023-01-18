from django.db import models

# Create your models here.
class DeviceModel(models.Model):
  name = models.CharField(max_length=100)


class ContentEventModel(models.Model):
  device_id = models.BigIntegerField()
  content_name = models.CharField(max_length=150)
  content_type = models.CharField(max_length=150)
  content_size  = models.CharField(max_length=150)
  start_time = models.TimeField()
  end_time = models.TimeField()