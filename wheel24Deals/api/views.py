from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.models import Vehicle
from .serializer import VehicleSerializer

@api_view(['GET'])
def get_vehicles(request):
    vehicles = Vehicle.objects.all()
    serializedData = VehicleSerializer(vehicles, many=True).data  # convert to json
    return Response(serializedData)

@api_view(['POST'])
def create_vehicle(request):
    data = request.data
    serializer = VehicleSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_vehicle(request, pk):
    try:
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)