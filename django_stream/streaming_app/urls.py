from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^stream/$', stream, name="stream"),
    url(r'^$', index, name="index")
]
