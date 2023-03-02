from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/',
         views.ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('farmer_lands/', views.FarmerLandAPIView.as_view(), name='farmer-lands'),
]
