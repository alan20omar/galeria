from django.shortcuts import render
from galeria.settings import BASE_DIR
from .models import *
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import os, json


def index(request):
    dirImages = os.path.join(BASE_DIR,'appgal','static','imagenes')
    print(dirImages)
    # imgList = os.listdir("C:/Users/alan_/Desktop/Proyecto/Galeria de imagenes/galeria/appgal/static/imagenes")
    imgList = os.listdir(os.path.join(BASE_DIR,'appgal','static','imagenes'))
    img={}
    for x in imgList:
        img[x]=f'/static/imagenes/{x}'
    dic={"imagenes":img}
    return render(request,'galeria.html',dic)

def saveImage(request):
    # data = json.loads(request.POST['data'])
    data = request.POST['nombre']
    image = request.FILES['image']
    print(image)
    # newGaleria = Galeria(
    #     image = image,
    #     name = data['nombre']
    # )
    return HttpResponse(status = 201)