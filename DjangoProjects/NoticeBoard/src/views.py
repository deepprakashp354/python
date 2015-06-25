from django.shortcuts import render
import datetime
# Create your views here.
from src.models import Event

def events(request):
	now=datetime.datetime.now() #python library(datetime).python class(datetime).datetime method(now)
	tmrw=datetime.date.today() + datetime.timedelta(days = 1)

	events_all = Event.objects.all # to get all the event and storing into the object
	events_today = Event.objects.filter(event_date__day = now.strftime("%d")) #filtering the object using the date
																#event_date__day gives the day only
																#These methods belongs to the python, strftime("%d") gives the day, strftime("%m") gives the month, strftime("%y") gives the year
	events_tom = Event.objects.filter(event_date__day = tmrw.strftime("%d"))
	return render(request, 'events.html',{'events_all' : events_all, 'events_today' : events_today,'events_tom' : events_tom}) # dictionary is passed to the template

def event_details(request, event_id):
	detail_event = Event.objects.get(pk = event_id) #pk stands for primary key
	return render(request, 'event_detail.html', {'detail_event' : detail_event})

