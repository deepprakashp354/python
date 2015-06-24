from django.conf import urls
from django.contrib import admin

from . import views

urlpatterns = [
	urls.url(r'hello$', views.index, name='index'),
	urls.url(r'hi$', views.hi, name='index'),

]