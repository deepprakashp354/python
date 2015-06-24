from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # taking request and giving response, index is not predefined
	return HttpResponse("This is a static one !!")

def hi(request): # taking request and giving response, index is not predefined
	return HttpResponse("Hi friends !!")