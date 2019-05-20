from django.shortcuts import render,redirect,HttpResponse
from memberapp.models import *
from userinfo.models import *
from cartinfo.models import *

# Create your views here.

#购物车信息
def cart_views(request):
    try:
        user_id = request.session['user_id']
        carts = Cartinfo.objects.filter(user_id=int(user_id))
        print(locals())
        return render(request,'cart.html',locals())
    except:
        return redirect('lg')


#添加商品进购物车
def cartin_views(request):
    id = request.GET['id']
    try:
        count = request.GET['countText']
    except:
        count = 1
    good = Goods.objects.get(id=int(id))
    if good:
        try:
            user_id = request.session['user_id']
            Cartinfo.objects.create(count=count,good_id=id,user_id=user_id)
        except:
            return redirect('lg')
    else:
        print('没有该商品')
    return redirect('/')

#商品移除购物车
def cartout_views(request):
    id = request.GET['id']
    print('要删除的商品ID为：',id)
    cart = Cartinfo.objects.filter(id=id)
    cart.delete()
    return HttpResponse('ok')