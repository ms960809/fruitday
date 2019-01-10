import logging
import sys

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password,check_password
from django.db import DatabaseError

auth_check = 'MarceArhutglsajdg;ladsjg;lasjgs;lajgals;jgdsl;jgdl;s'
# Create your views here.
def register_in(request):
    return render(request,'register.html')


def register_(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.uphone = request.POST.get('phone')
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
            password = make_password(request.POST.get('pwd1'),auth_check,'pbkdf2_sha1')
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


def login_views(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        phone = request.POST['name']
        pwd = request.POST['pwd']
        try:
            user = UserInfo.objects.get(uphone=phone,isban='False')
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


def login_out(request):
    try:
        if request.session['user_name']:
            del request.session['user_name']
            del request.session['user_id']
            return redirect('/')
        else:
            return redirect('/')
    except:
        print('出现异常')
        sys.exit(0)