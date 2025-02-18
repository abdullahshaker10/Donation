from django.db import models

from root.campaigns.models import Campaign
from root.donations.enums import DonationStatus, TransactionStatus
from root.users.models import User

# Create your models here.
class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    status  = models.CharField(max_length=255, choices=DonationStatus.name_value_choices(), default=DonationStatus.PENDING.name)
    def __str__(self):
        return f"Donation {self.id} "
class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=TransactionStatus.name_value_choices(), default=TransactionStatus.PENDING.name)
    donation = models.OneToOneField(Donation, on_delete=models.CASCADE)
    def __str__(self):
        return f"Transaction {self.id} - Donation{self.donation.id}"