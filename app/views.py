from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *

from django.db.models import Q
from django.http import HttpResponse

def display_topic(request):
    #topics=Topic.objects.all()
    #topics=Topic.objects.get(topic_name='Dance')

    return render(request,'display_topic.html',context={'topics':topics})


def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='Dance')
    #webpages=Webpage.objects.all().order_by('name')# in Ascending order based on Aschii Value
    #webpages=Webpage.objects.all().order_by('-name')# in Descending order based on Aschi value
    #webpages=Webpage.objects.all().order_by(Length('name'))# Ascending order based on Length
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    #webpages=Webpage.objects.filter(topic_name='Dance').order_by('url')
    #webpages=Webpage.objects.all()[0:5]
    #webpages=Webpage.objects.exclude(topic_name='Dance')
    #webpages=Webpage.objects.filter(name__startswith='A')
    #webpages=Webpage.objects.filter(name__endswith='a')
    #webpages=Webpage.objects.filter(name__contains='a')
    #webpages=Webpage.objects.filter(Q(topic_name='Dance') & Q(name='Jerome'))
    #webpages=Webpage.objects.filter(Q(topic_name='Dance'))




    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access(request):
    #access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date='1995-01-21')
    #access=Access_Records.objects.filter(date__year='1979')# compares only year
    #access=Access_Records.objects.filter(date__month='01')# compares only month
    #access=Access_Records.objects.filter(date__day='19') # comares only day
    #access=Access_Records.objects.filter(date__gt='1995-01-21')
    #access=Access_Records.objects.filter(date__year__gt='1970')
    #access=Access_Records.objects.filter(date__gte='1995-01-21')
    #access=Access_Records.objects.filter(date__lt='1995-01-21')
    #access=Access_Records.objects.filter(date__lte='1995-01-21')
    
    
    



    return render(request,'displayaccess.html',context={'access':access})


def deleteweb(request):
    #Webpage.objects.filter(topic_name='sports').delete()
    #return HttpResponse('data has been deleted successfully')
    Webpage.objects.filter(name='Amy').delete()
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})


def updateweb(request):
    #Webpage.objects.filter(name='Pual').update(url='https://Paul.com',topic_name='singing')
    #Webpage.objects.filter(name='python').update(url='https://Paul.com',topic_name='singing')
    #Webpage.objects.update_or_create(name='Pual',defaults={'url':'http://haipual.info.in'})
    t=Topic.objects.get_or_create(topic_name='singing')[0]
    Webpage.objects.update_or_create(name='Dhoni',topic_name=t,defaults={'url':'http://Dhoni.info.in','topic_name':t})
    
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})












