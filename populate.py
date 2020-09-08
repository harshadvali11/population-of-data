# creating django environment
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project13.settings')

# setting up the features of django

import django
django.setup()
# importing models
from app.models import *
from faker import Faker
f=Faker()
import random
topics=['Dance','singing','cricket','sports']

def Add_topics():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def Add_webpage(webpagename,url):
    topic_name=Add_topics()
    w=Webpage.objects.get_or_create(topic_name=topic_name,name=webpagename,url=url)[0]
    w.save()
    return w

def Add_records(webpagename,url,date):
    name=Add_webpage(webpagename,url)
    a=Access_Records.objects.get_or_create(name=name,date=date)[0]
    a.save()
    
n=int(input('enter number of rows to be inserted'))

def Add_data(n):
    for i in range(n):
        fakename=f.first_name()
        fakeurl=f.url()
        fakedate=f.date()

        Add_records(fakename,fakeurl,fakedate)

if __name__=='__main__':
    print('population hass started')
    Add_data(n)
    print('population has ended')



















