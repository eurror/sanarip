from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Land
from .serializers import LandSerializer, RegisterSerializer
from .models import User


class FarmerLandAPIView(generics.ListAPIView):
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Land.objects.filter(farmer_name=self.request.user.username)


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response("Successfully registered", 201)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(
            email=email, activation_code=activation_code).first()
        if not user:
            return Response("User doesn't exist", 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', 200)
