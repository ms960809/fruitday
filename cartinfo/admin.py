from django.contrib import admin
from .models import *

# Register your models here.

class CartinfoAdmin(admin.ModelAdmin):
    list_display = ['id','count','good_id','user_id']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','orderNo','ads','acot','acount','cals','orderStatus']


admin.site.register(Cartinfo,CartinfoAdmin)
admin.site.register(Order,OrderAdmin)