from django.urls import path
from . import views

urlpatterns = [
    path('weather-data/', views.WeatherDataList.as_view(), name='weatherdata-list'),
    path('weather-data/<int:pk>/', views.WeatherDataDetail.as_view(), name='weatherdata-detail'),
]

