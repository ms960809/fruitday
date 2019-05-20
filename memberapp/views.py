from django.shortcuts import render
from .models import *
# Create your views here.


#主页信息
def index_views(request):
    good_list = GoodsType.objects.all()
    return render(request,'index.html',locals())


#商品详情
def desc_views(request,id=None):
    print('ID',id)
    good = Goods.objects.get(id=id)
    return render(request,'desc.html',locals())