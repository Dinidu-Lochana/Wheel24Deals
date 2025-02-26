from django.urls import path
from .views import get_vehicles ,create_vehicle,get_vehicle, delete_vehicle, update_vehicle

urlpatterns = [
    path('vehicles/' , get_vehicles, name='get_vehicles'),
    path('vehicles/create' , create_vehicle , name='create_vehicle'),
    path('vehicles/<int:pk>/', get_vehicle, name='get_vehicle'),
    path('deletevehicle/<int:pk>/', delete_vehicle, name='delete_vehicle'),
    path('updatevehicle/<int:pk>/', update_vehicle, name='update_vehicle'),

]  