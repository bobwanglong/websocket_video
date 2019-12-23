from django.urls import path
from .import consumers


websocket_urlpatterns = [
    # path('ws/video', consumers.UploadVideo),
    path('ws/chats', consumers.ChatConsumer),
    path('ws/chat', consumers.UploadVideo),

]
