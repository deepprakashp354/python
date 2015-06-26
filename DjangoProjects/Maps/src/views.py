from django.shortcuts import render
import urllib.request
import json
from django.http import HttpResponse
# Create your views here.

def maps(request):
	map_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=arera%20colony&key=AIzaSyD9brbOk2dqsz5FkxLdj9hokOwdtWNI7Bk'
	map_url_open = urllib.request.Request(map_url)
	map_url_read = urllib.request.urlopen(map_url_open) #opens the url server
	map_url_read = map_url_read.read()  #loading the data
	map_url_load = json.loads(map_url_read.decode("utf-8"))   #loading the json data returned by the API, decode() method decodes it into general form
	maps_db=map_url_load
	maps_data_longitude = maps_db['results'][0]['geometry']['location']['lng']
	maps_data_latitude = maps_db['results'][0]['geometry']['location']['lat']

	return render(request,'maps_display.html',{'longitude' : maps_data_longitude,'latitude' : maps_data_latitude})