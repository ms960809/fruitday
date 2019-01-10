from django.conf.urls import url
from .views import *
# create urls

urlpatterns = [
    url(r'^register/$',register_in,name='reg'),
    url(r'^login/$',login_views,name='lg'),
    url(r'^reg/$',register_,name='regs'),
    url(r'^lgout$',login_out,name='lgt')

]