from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='Measurement')
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)