from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.shortcuts import render

from .helpers import stream_json


def index(request):
    return render(request, "index.html")


def stream(request):
    return StreamingHttpResponse(stream_json())
