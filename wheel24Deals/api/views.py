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
    
@api_view(['PUT'])
def update_vehicle(request, pk):
    try:
        vehicle = Vehicle.objects.get(id=pk)  
        data = request.data
        serializer = VehicleSerializer(vehicle, data=data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)

    

@api_view(['DELETE'])
def delete_vehicle(request, pk):
    try:
        vehicle = Vehicle.objects.get(id=pk)
        vehicle.delete()
        return Response( status=status.HTTP_200_OK)
    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_vehicle_by_type(request, type):
    try:
        vehicles = Vehicle.objects.filter(type=type)  
        if vehicles.exists():
            serializer = VehicleSerializer(vehicles, many=True)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No vehicles found for this type"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)