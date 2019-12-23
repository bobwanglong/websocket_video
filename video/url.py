
from django.urls import path
from video.views import chat, video_upload

urlpatterns = [
    # path('chat', chat, name='chat-url'),
    path('upload', video_upload, name='video_upload-url')
]