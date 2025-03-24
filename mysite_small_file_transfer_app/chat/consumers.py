# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


import cv2
import numpy as np

# # Assume `binary_data` is the received image data
# def display_image_from_binary(binary_data):
#     # Convert binary data to a 1D NumPy array (dtype=uint8)
#     nparr = np.frombuffer(binary_data, np.uint8)
    
#     # Decode the NumPy array to an image
#     image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#     # Display the image
#     if image is not None:
#         cv2.imshow('Received Image', image)
#         cv2.waitKey(0)  # Wait for key press to close window
#         cv2.destroyAllWindows()
#     else:
#         print("❌ Failed to decode image. Data may be corrupted.")

# # Example usage: Assuming `binary_data` is the data from WebSocket or file
# with open('received_image.jpg', 'rb') as file:
#     binary_data = file.read()

# display_image_from_binary(binary_data)




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            try:
                metadata_str, image_data = bytes_data.split(b'||', 1)
                print(image_data)
                # metadata = json.loads(metadata_str.decode('utf-8'))

                # self.send(text_data=json.dumps({
                #     'message': metadata.get('message', ''),
                #     'username': metadata.get('username', 'Anonymous'),
                #     'image_info': metadata.get('image', None)
                # }))

                # self.send(bytes_data=image_data)  # ✅ Binary data sent correctly

            except Exception as e:
                print(f"❌ Error processing data: {e}")

        # text_data_json = json.loads(text_data)
        # # message = text_data_json["message"]


        # print(text_data_json.get('image', None))

        # # Send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name, 
        #     # {"type": "chat.message", "message": message}
        #     {
        #         'type': 'chat_message',
        #         'message': text_data_json.get('message', ''),
        #         'username': text_data_json.get('username', 'Anonymous'),
        #         'image_info': text_data_json.get('image', None)
        #     }
        # )

    # Receive message from room group
    def chat_message(self, event):
        # message = event["message"]
        self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
            'image_info': event.get('image_info', None)
        }))

        # Send message to WebSocket
        # self.send(text_data=json.dumps({"message": message}))


    # async def image_data(self, event):
    #     # Send image data as binary back to the frontend
    #     await self.send(bytes_data=event['image_data'])