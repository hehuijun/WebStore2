from django.shortcuts import render
from django.http import HttpResponse
from commodity.models import Commondity
from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

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


def listing(request):
    contact_list = Commondity.objects.all()
    paginator = Paginator(contact_list, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'contacts': contacts})