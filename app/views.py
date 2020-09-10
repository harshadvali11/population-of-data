from django.shortcuts import render

# Create your views here.
from app.models import *


def display_topic(request):
    #topics=Topic.objects.all()
    #topics=Topic.objects.get(topic_name='Dance')

    return render(request,'display_topic.html',context={'topics':topics})


def display_webpage(request):
    #webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='Dance')
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.filter(topic_name='Dance').order_by('url')
    #webpages=Webpage.objects.all()[0:5]
    #webpages=Webpage.objects.exclude(topic_name='Dance')
    #webpages=Webpage.objects.filter(name__startswith='A')
    #webpages=Webpage.objects.filter(name__endswith='a')
    webpages=Webpage.objects.filter(name__contains='a')



    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access(request):
    #access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date='1995-01-21')
    access=Access_Records.objects.filter()

    return render(request,'displayaccess.html',context={'access':access})


















