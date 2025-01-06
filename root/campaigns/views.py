
from root.campaigns.models import Campaign
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from root.campaigns.serializers import CampaignSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]
