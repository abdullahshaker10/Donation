from django.urls import path,include
from .views import CampaignViewSet
from rest_framework.routers import DefaultRouter

campaign_router = DefaultRouter()
campaign_router.register(r'', CampaignViewSet, basename='campaign')

urlpatterns = [
    path('', include(campaign_router.urls)),
]