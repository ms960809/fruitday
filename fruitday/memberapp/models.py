from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title = models.CharField('类名称',max_length=30)
    desc = models.CharField('类描述',max_length=200,default='商品描述')
    picture = models.ImageField('商品图片',upload_to='static/img/good_type',default='normal.png')
    isdelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods_type'
        verbose_name = '商品类信息表'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    title = models.CharField('商品名称',max_length=30)
    price = models.DecimalField('商品价格',max_digits=8,decimal_places=2)
    unit = models.CharField('单位',max_length=20,default='500g')
    desc = models.CharField('描述',max_length=1000,)
    detail = models.CharField('商品描述',max_length=2000)
    picture = models.ImageField('商品图片',upload_to='static/img/goods',default='normal.png')
    type = models.ForeignKey(GoodsType,on_delete=models.CASCADE,verbose_name='类型')
    isdelete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return '/detail/?good={}'.format()

    class Meta:
        db_table='goods'
        verbose_name = '商品信息表'
        verbose_name_plural=verbose_name