from django.shortcuts import render
from django.core.cache import  cache

# Create your views here.
from django.http import HttpResponse
import time
from .tasks import SendEmail

def send_email(request):
    SendEmail.delay()
    return HttpResponse("<h1>done sending</h1>")

# def test(request):
#     if cache.get("test_delay_api") is None:
#         response=request.get