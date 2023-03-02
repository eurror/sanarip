from django.urls import path
from .views import FarmerLandAPIView

urlpatterns = [
    path('farmer_lands/', FarmerLandAPIView.as_view(), name='farmer-lands'),
]
