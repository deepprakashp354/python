from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.events, name='events'),
	url(r'^(?P<event_id>\d+)/$',views.event_details, name='event_details'), #(?P<>) to create a variable name
															  # \d+ means it can accept any digit 0-9\
															  # \ is the escape sequence and d+ means digits
]