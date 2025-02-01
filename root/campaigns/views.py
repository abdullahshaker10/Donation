
from root.campaigns.models import Campaign
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from root.campaigns.serializers import CampaignSerializer
from root.users.utils import has_permission

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]

    @has_permission('can_edit_campaign')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

