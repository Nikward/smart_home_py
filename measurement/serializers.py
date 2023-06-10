from rest_framework import serializers

from measurement.models import Sensors, TemperatureMeasurement


# TODO: опишите необходимые сериализаторы


class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = TemperatureMeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensors
        fields = ['id', 'name', 'description', 'measurements']
