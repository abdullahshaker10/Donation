import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Campaign

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Campaign)
def notify_campaign_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New campaign created: {instance.name}")
        try:
            channel_layer = get_channel_layer()
            if channel_layer is None:
                logger.error("Could not get channel layer!")
                return
                
            logger.info(f"Got channel layer: {channel_layer}")
            
            message = {
                "type": "notification_message",
                "message": f"New campaign created: {instance.name}",
                "unread_count": 1
            }
            logger.info(f"Sending message to channel layer: {message}")
            
            async_to_sync(channel_layer.group_send)(
                "notifications",
                message
            )
            logger.info("Notification sent to channel layer successfully")
            
        except Exception as e:
            logger.error(f"Error sending notification: {str(e)}", exc_info=True) 