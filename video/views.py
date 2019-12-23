from django.shortcuts import render, HttpResponse
import json


# Create your views here.
def chat(request):
    return render(request, 'chat/index.html')


def video_upload(request):
    if request.method == 'POST':
        print(request.FILES)
        file_obj = request.FILES.get('myfile')

        with open(file_obj.name, 'wb') as f:
            for line in file_obj.chunks():
                f.write(line)

        print(request.POST)
        return HttpResponse('ok')

    return render(request, 'video/video.html')


def hello(request):
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        return HttpResponse('ok')
    return render(request, 'hello.html')
