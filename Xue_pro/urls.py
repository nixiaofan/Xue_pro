"""Xue_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView
from django.views.static import serve

from Xue_pro.settings import MEDIA_ROOT
from users import views as v1

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^users/$', include('users.urls', namespace='users')),
    url(r'^login/$', v1.UserLogin, name='login'),
    url(r'^register/$', v1.RegisterView.as_view(), name='register'),
    #验证图
    url(r'^captcha/', include('captcha.urls')),
    #------------以上是users的url---以下是org和course的url-----------------
    url(r'^org/', include('organization.urls', namespace='org')),
    url(r'^course/', include('course.urls', namespace='course')),

    # 配置静态文件的处理
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),



]
