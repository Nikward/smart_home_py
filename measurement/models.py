from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement) и сделай миграцию
class Sensors(models.Model):
    name = models.CharField(max_length=20, verbose_name='Датчик')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')


class TemperatureMeasurement(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата')