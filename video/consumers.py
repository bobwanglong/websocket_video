from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync
import json
import os


class UploadVideo(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'China_Mobile_video'
        # 连接
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # 断开
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        print('收到的二进制文件信息：', bytes_data)
        print('收到的文本信息信息：', text_data)
        file_name = text_data
        if file_name:
         # 检查是否有文件
            if not os.path.isfile(file_name):
        # 没有就创建文件
                with open(file_name, 'wb') as f:
                    f.close()
        if bytes_data:
            with open("3.mp4", "wb") as f:
                f.write(bytes_data)
        # with open(file_name, 'wb') as f:
        #     f.write(bytes_data)
    # json 序列化
    #     text_data_json = json.loads(text_data)
    #     print(text_data_json)
        # video_message = text_data_json['video_message']
        # text_data_json = json.loads(text_data)

        # video_message = text_data_json['message']
        # file = text_data_json['byte_name']
        # print(video_message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                # 'type': 'video_message',
                'type': 'chat_message',
                # 'message': video_message
            }
        )

    # async def video_message(self, event):
    async def chat_message(self, event):
        # message = 'anonymous_user' + event['video_message']
        # message = 'anonymous_user: ' + event['message']

        print('back')
        # WebSocket send
        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))
        # print('这是video的信息', message)


# chat
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'China_Mobile'
        # Join room group
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        # self.accept()
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        pass

    async def receive(self, text_data=None, bytes_data=None):
        # text_data_json = json.loads(text_data)
        # message = 'python咖啡吧：' + text_data_json['message']
        # print("这是chat的信息：",message)
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = 'China-Mobile：' + event['message']

        # Send message to WebSocket
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        await self.send(text_data=json.dumps({
            'message': message

        }))
        print('这是chat的聊天信息', message)
