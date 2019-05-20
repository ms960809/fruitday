import logging
import sys
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import *
# from cartinfo.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password,check_password
from django.db import DatabaseError

auth_check = 'MarceArhutglsajdg;ladsjg;lasjgs;lajgals;jgdsl;jgdl;s'
# Create your views here.
def register_in(request):
    return render(request,'register.html')

#注册模块
def register_(request):
    if request.method == 'POST':
        #用户对象
        new_user = UserInfo()
        new_user.uphone = request.POST.get('phone')
        #判断测试时手机号是否已被使用
        try:
            a = UserInfo.objects.filter(uphone=new_user.uphone)
            if a :
                print('手机号已存在')
                return render(request,'register.html',{'message':'手机号已存在'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd1') != request.POST.get('pwd2'):
            print('密码不一致')
            return render(request,'register.html',{'message':'密码不一致'})
        else:
            #对密码进行加密
            password = make_password(request.POST.get('pwd1'),auth_check,'pbkdf2_sha1')
            #将用户信息存入数据库
            new_user.uname = request.POST.get('name')
            new_user.upassword = password
            new_user.uemail = request.POST.get('email')
            new_user.uphone = request.POST.get('phone')
            try:
                new_user.save()
            except DatabaseError as e:
                logging.warning('aaaaa'+e)
    print('验证成功')
    return render(request,'login.html',{'message':'注册成功'})


#登录模块
def login_views(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        phone = request.POST['name']
        pwd = request.POST['pwd']
        try:
            #查询是否有该账号，并且账号是否被禁用
            user = UserInfo.objects.get(uphone=phone,isban='False')
            #核对密码是否正确
            pwd1 = check_password(pwd,user.upassword)
            if phone == user.uphone and pwd1:
                request.session['user_name'] = user.uname
                request.session['user_id'] = user.id
                resp = redirect('/')
                resp.set_cookie('user_name',user.uname,60*3)
                resp.set_cookie('user_id',user.id,60*3)
                return resp
            else:
                return render(request,'login.html',{'message':'账号或密码错误'})
        except:
            return render(request,'login.html',{'message':'没有该手机号'})

#退出登录
def login_out(request):
    try:
        if request.session['user_name']:
            #删除session
            del request.session['user_name']
            del request.session['user_id']
            return redirect('/')
        else:
            return redirect('/')
    except:
        print('出现异常')
        sys.exit(0)

#用户个人中心
def user_info(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = UserInfo.objects.get(id=user_id)
        try:
            address = Address.objects.get(user_id=user_id)
        except:
            pass
        print('-----------------------------------------')
        print(locals())
        print('-----------------------------------------')
        return render(request,'userinfo.html',locals())
    elif request.method == 'POST':
        try:
            aid = request.POST['aid']
            Address.objects.get(id=aid)
        except:
            #没有用户信息则增加用户地址信息
            id = request.POST['id']
            sname = request.POST['sname']
            address = request.POST['address']
            sphone = request.POST['sphone']
            ads = Address()
            ads.user = UserInfo.objects.get(id=id)
            ads.aname = sname
            ads.address = address
            ads.cellphone = sphone
            try:
                ads.save()
                print('增加成功！')
                print(request.POST)
            except DatabaseError as e:
                logging.warning('aaaaa' + e)
        else:
            #修改用户地址等信息
            aid = request.POST['aid']
            id = request.POST['id']
            sname = request.POST['sname']
            address = request.POST['address']
            sphone = request.POST['sphone']
            ads = Address.objects.get(id=aid)
            ads.user = UserInfo.objects.get(id=id)
            ads.aname = sname
            ads.address = address
            ads.cellphone = sphone
            try:
                ads.save()
                print('修改成功')
                print(request.POST)
            except DatabaseError as e:
                logging.warning('aaaaa' + e)
        #对url反向解析
        url = reverse('uinfo')
        return redirect(url)