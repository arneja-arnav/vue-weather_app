from django.db import models

class WeatherData(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Weather Data for {self.location}'

