from django.shortcuts import render
from .models import *
# Create your views here.


def index_views(request):
    good_list = GoodsType.objects.all()
    return render(request,'index.html',locals())


def desc_views(request,id=None):
    print('ID',id)
    good = Goods.objects.get(id=id)
    return render(request,'desc.html',locals())