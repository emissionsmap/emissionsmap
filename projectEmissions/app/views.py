from django.shortcuts import render
from geospatial.main import mapPlot

# Create your views here.

def home(req):
    m = mapPlot()
    context={
        'map':m
    }

    return render(req,'index.html',context)
