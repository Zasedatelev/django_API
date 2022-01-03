from rest_framework import generics
from models import Sensor, Measurement
from serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class APISensorCreate(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class APISensorUpdate(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class APISensorMeasurement(generics.UpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class APISensorList(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class APISensorRetrieve(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
