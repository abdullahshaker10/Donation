from django.db import models
from django.core.cache import cache

from root.campaigns.enums import CampaignStatus

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    goal_currency = models.CharField(max_length=255,choices=[("USD", "USD"), ("EGP", "EGP")],default="EGP")
    status = models.CharField(max_length=255, choices=CampaignStatus.name_value_choices(), default=CampaignStatus.INACTIVE.name)
    
    @classmethod
    def get_cached_data_as_object(self,id):
        from root.campaigns.serializers import CampaignSerializer

        cache_key = f"campaign:{id}"
        cached_data = cache.get(cache_key)
        if not cached_data:
            object = self.objects.get(id=id)
            cache.set(cache_key, CampaignSerializer(object).data, timeout=3600) 
            cached_data = cache.get(cache_key)
    @classmethod
    def get_cached_data_as_query_set(self,id):

        cache_key = f"campaign_query_set:{id}"
        cached_data = cache.get(cache_key)
        if not cached_data:
            object = self.objects.get(id=id)
            cache.set(cache_key, object, timeout=3600) 
            cached_data = cache.get(cache_key)

        return cached_data
    def __str__(self):
        return self.name