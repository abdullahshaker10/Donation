from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CampaignViewSet

campaign_router = DefaultRouter()
campaign_router.register(r"", CampaignViewSet, basename="campaign")

urlpatterns = [
    path("", include(campaign_router.urls)),
]
