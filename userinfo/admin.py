from django.contrib import admin
from .models import *

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','uphone','uname','uemail','ujifen','udatetime','isban']
    list_display_links = ['uname']
    list_editable = ['uemail','ujifen','isban']
    search_fields = ['uname','uemail']
    date_hierarchy = 'udatetime'
    fieldsets = (('基本选项',{'fields':('uphone','uname','uemail','ujifen',)})\
                     ,('高级选项',{'fields':('isban',),'classes':('collapse',)}))

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','aname','user','address','cellphone']
    list_display_links = ['aname','address']
    list_editable = ['cellphone']
    search_fields = ['address','aname']
    fieldsets = (('基本选项',{'fields':('aname','user')}),\
                 ('高级选项',{'fields':('cellphone','address'),'classes':('collapse',)}))


admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Address,AddressAdmin)


