from rest_framework import serializers

from root.campaigns.models import Campaign
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [ 'name', 'description', 'start_date', 'end_date', 'created_at', 'updated_at', 'goal_amount', 'goal_currency', 'status']
        kwargs = {"read_only": ["created_at", "updated_at","start_date","end_date","status"]}
        