import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

logger = logging.getLogger(__name__)

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connection attempt")
        try:
            # Check if channel_layer exists
            if not hasattr(self, 'channel_layer'):
                logger.error("No channel layer configured!")
                return
                
            logger.info(f"Channel layer: {self.channel_layer}")
            
            # Join the notifications group
            await self.channel_layer.group_add(
                "notifications",
                self.channel_name
            )
            await self.accept()
            logger.info("WebSocket connection established successfully")
            
            # Send a test message to verify the connection
            await self.send(text_data=json.dumps({
                'type': 'notification',
                'message': 'WebSocket connected successfully',
                'unread_count': 0
            }))
            
        except Exception as e:
            logger.error(f"Error in WebSocket connection: {str(e)}")
            raise

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected with code: {close_code}")
        try:
            await self.channel_layer.group_discard(
                "notifications",
                self.channel_name
            )
        except Exception as e:
            logger.error(f"Error in WebSocket disconnection: {str(e)}")

    async def receive(self, text_data):
        logger.info(f"Received WebSocket message: {text_data}")
        try:
            data = json.loads(text_data)
            if data['type'] == 'mark_read':
                logger.info("Processing mark_read message")
                # Handle marking notifications as read
                # You can add database logic here
                pass
        except Exception as e:
            logger.error(f"Error processing received message: {str(e)}")

    async def notification_message(self, event):
        logger.info(f"Received notification event: {event}")
        try:
            message = {
                'type': 'notification',
                'message': event['message'],
                'unread_count': event.get('unread_count', 1)
            }
            logger.info(f"Sending message to client: {message}")
            await self.send(text_data=json.dumps(message))
            logger.info("Notification sent successfully")
        except Exception as e:
            logger.error(f"Error sending notification: {str(e)}")
            raise