from django.urls import path
from .views import get_vehicles ,create_vehicle,get_vehicle

urlpatterns = [
    path('vehicles/' , get_vehicles, name='get_vehicles'),
    path('vehicles/create' , create_vehicle , name='create_vehicle'),
    path('vehicles/<int:pk>/', get_vehicle, name='get_vehicle'),

]