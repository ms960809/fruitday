from django.db import models
from userinfo.models import *
from memberapp.models import *

# Create your models here.

ORDERSTATUS = (
    (1,'未支付'),
    (2,'已支付'),
    (3,'订单取消'),
)

class Cartinfo(models.Model):
    user = models.ForeignKey(UserInfo,db_column='user_id',on_delete=models.CASCADE)
    good = models.ForeignKey(Goods,db_column='good_id',on_delete=models.CASCADE)
    count = models.IntegerField('商品数量',db_column='cart_count')

    def __str__(self):
        return self.user.uname

    class Meta:
        db_table='cartinfo'
        verbose_name='购物车表'
        verbose_name_plural=verbose_name


class Order(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    orderNo= models.CharField('订单编号',max_length=200)
    ads = models.CharField('收件人',max_length=200)
    acot = models.IntegerField('总数')
    acount  = models.IntegerField('价格')
    cals = models.TextField('订单详情',blank=True,null=True)
    orderStatus = models.IntegerField('是否提交',blank=True,default=1,choices=ORDERSTATUS)

    def __str__(self):
        return self.user.uname

    class Meta:
        db_table='order'
        verbose_name='订单表'
        verbose_name_plural=verbose_name

    def get_orderStatusDisplay(self):
            # 'u'表示unicode编码
        if self.orderStatus == 1:
            return u'未支付'
        elif self.orderStatus == 2:
            return u'已支付'
        elif self.orderStatus == 3:
            return u'订单取消'
        else:
            return u''