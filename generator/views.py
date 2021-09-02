from django.shortcuts import render
from django.http import HttpResponse
import pyqrcode
import png
from qrcode import *
from django.core.files import File
from PIL import Image
import PIL

# Create your views here.

def index(request):
    return render(request,'index.html');


# url = None
def generator(request):
    # global url
    url  = request.POST.get('url')
    image = pyqrcode.create(url)
    image.png("qrcode.png",scale=8)
    image.show()
    return render(request,'index.html',{'url':image})
