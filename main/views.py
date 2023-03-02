from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Land
from .serializers import LandSerializer


class FarmerLandAPIView(generics.ListAPIView):
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # get the authenticated user's lands only
        return Land.objects.filter(farmer_name=self.request.user.username)
