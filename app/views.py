from django.shortcuts import render

# Create your views here.
from app.models import *


def display_topic(request):
    #topics=Topic.objects.all()
    topics=Topic.objects.get(topic_name='Dance')
    return render(request,'display_topic.html',context={'topics':topics})


def display_webpage(request):
    #webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(topic_name='Dance')

    return render(request,'display_webpage.html',context={'webpages':webpages})