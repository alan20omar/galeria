from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):
    imgList = os.listdir("C:/Users/alan_/Desktop/Proyecto/Galeria de imagenes/galeria/appgal/static/imagenes")
    img={}
    for x in imgList:
        img[x]=f'/static/imagenes/{x}'

    dic={"imagenes":img}
    return render(request,'galeria.html',dic)

