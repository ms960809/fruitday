from django.contrib import admin
from .models import *

# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','price','isdelete','type']
    list_editable = ['price','isdelete','desc']
    search_fields = ['title','price','type']


class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','isdelete']
    list_editable = ['desc','isdelete','desc']
    search_fields = ['title','desc']


admin.site.register(Goods,GoodsAdmin)
admin.site.register(GoodsType,GoodsTypeAdmin)