from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.models import Vehicle
from .serializer import VehicleSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializer import UserSerializer, LoginSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({
    'refresh': str(refresh),
    'access': access_token,
    'message': 'User created successfully'
}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
    return Response({
    'refresh': str(refresh),
    'access': access_token,
    'username': user.username,
    'message': 'User logged in successfully'
}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_vehicles(request):
    vehicles = Vehicle.objects.all()
    serializedData = VehicleSerializer(vehicles, many=True).data  # convert to json
    return Response(serializedData)

@api_view(['POST'])
def create_vehicle(request):
    data = request.data
    serializer = VehicleSerializer(data=request.data)  # Correct
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
