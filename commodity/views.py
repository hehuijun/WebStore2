from django.http import HttpResponse
from commodity.models import Commondity
from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, Paginator


# Create your views here.

# def list(request):#没有分页
#     post_list = Commondity.objects.all()#获取全部对象
#     return render(request,'list.html',{'post_list':post_list})

def list(request):#系统默认的Paginator
    limit = 3  # 每页显示的记录数
    post_list = Commondity.objects.all()#获取全部对象
    paginator = Paginator(post_list, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        post_list = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        post_list = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        post_list = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render(request,'list.html', {'post_list': post_list})
def index(request):
    post_index = Commondity.objects.all()[:8]#获取全部对象,仅显示前8条数据
    return render(request,'index.html',{'post_index':post_index})

def detail(request, id):
    try:
        post = Commondity.objects.get(id=str(id))
    except Commondity.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})

