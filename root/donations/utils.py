from django.db import transaction as db_transaction

from root.donations.models import Donation, Transaction

 

def process_donation(user, campaign, amount):
    donation = Donation.objects.create(  
        user=user,
        campaign=campaign,
        amount=amount,
        status='pending'  
    )

    try:
        with db_transaction.atomic():
            transaction = Transaction.objects.create(
                donation=donation,
                amount=amount,
                status='pending'
            )


            process_payment(transaction)

            transaction.status = 'completed'
            transaction.save()

            donation.status = 'completed'
            donation.save()

            return donation

    except Exception as e:
        donation.status = 'failed'
        donation.save()

        raise e  
def process_payment(transaction):
    pass
