from django.db import models
import datetime


# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=50,verbose_name='用户名称')
    upassword = models.CharField(max_length=200,verbose_name='用户密码')
    uemail = models.EmailField(verbose_name='用户邮箱')
    uphone = models.CharField('手机号',max_length=50,null=True)
    udatetime = models.DateTimeField(verbose_name='注册时间',auto_now_add=True)
    isban = models.BooleanField(verbose_name='是否禁用',default=False)

    def __str__(self):
        return self.uname

    class Meta:
        db_table='userinfo'
        verbose_name='用户信息表'
        verbose_name_plural = verbose_name


class Address(models.Model):
    aname = models.CharField(max_length=40,verbose_name='姓名')
    address = models.CharField('收站点',max_length=150)
    cellphone = models.CharField('手机号码',max_length=11)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE,verbose_name='用户')

    def __str__(self):
        return self.aname

    class Meta:
        db_table = 'address'
        verbose_name = '收货地址表'
        verbose_name_plural=verbose_name
