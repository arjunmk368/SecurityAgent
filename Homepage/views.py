import json
import threading
import cv2
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from imutils.video import VideoStream
from .models import Table
from django.views.decorators.csrf import csrf_exempt
from jinja2 import Environment, FileSystemLoader

object_list = []


def index(request):
    global object_list
    object_list = []
    a = 2
    if (a == 1):
        Query_response = Table.objects.all().get(Age='17')
    else:
        Query_response = Table.objects.all().get(Age='16')

    return render(request, 'Homepage/index.html', {'Query_response': Query_response})


@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    print(req)
    action = req.get('queryResult').get('action')
    print(action)
    fulfillmentText = {'fulfillment': 'This is Django test response from webhook'}
    return JsonResponse(fulfillmentText, safe=False)


@csrf_exempt
def DBUpdate(request):
    request_msg = json.loads(request.body)
    person = request_msg['queryResult']['parameters']['name']
    object = Table.objects.all().get(Name_of_the_User=person)
    object_list.append(object)
    if (request_msg['queryResult']['parameters']['commands'] == 'positive_commands'):
        object.Allowed = True
        print("1")
        print(request_msg['queryResult']['parameters'])
    else:

        object.Allowed = False
        print(2)
        print(request_msg['queryResult']['parameters'])
    object.save()
    msg = {
        "fulfillment_text": "Hii"
    }

    return JsonResponse(msg, safe=False)


def result(request):
    global object_list
    context = {'object_list': object_list}
    return render(request, 'Homepage/sample.html', context=context)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        print(self.video)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


class VideoCamera2(object):
    def __init__(self):
        self.video = VideoStream(src=0).start()
        print(self.video)
        self.frame = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.stop()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            self.frame = self.video.read()


# cam = VideoCamera2()


def gen(camera):
    while True:
        frame = cam.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip_page
def livefe(request):
    global cam
    print('Yes')
    print(cam.video)
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
