from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer

class WeatherDataList(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class WeatherDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

