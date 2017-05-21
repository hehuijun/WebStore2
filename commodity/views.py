from django.shortcuts import render
from django.http import HttpResponse
from commodity.models import Commondity
from datetime import datetime
from django.http import Http404


# Create your views here.

def home(request):
    #return  HttpResponse('Hello World!')
    post_list = Commondity.objects.all()#获取全部对象
    return render(request,'home.html',{'post_list':post_list})

def detail(request, id):
    try:
        post = Commondity.objects.get(id=str(id))
    except Commondity.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})
