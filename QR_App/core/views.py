from django.shortcuts import render
from .utils import embed_QR
# Create your views here.
import os
import base64


def menu(request):
    return render(request, 'base.html')


def create(request):
    url = request.POST['url_input']
    name = request.POST['qr_name']
    name += ".png"
    embed_QR(url, name)
    with open(name, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return render(request, 'home.html', {'image': image_data})


def home(request):
    return render(request, 'home.html')
