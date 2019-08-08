import xadmin
from xadmin import views

from .models import *


class BaseSettings(object):
    '''配置主题功能'''
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    '''更改全局配置,标题和页脚'''
    site_title = 'Xue'
    site_footer = 'XueOnline'




class EmailVerifyRecordAdmin(object):
    '''自定义显示列表、搜索框和筛选框'''
    list_display = ['code', 'mail', 'send_type', 'send_time']
    search_fields = ['code', 'mail']
    list_filter = ['code', 'mail']




xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(PageBanner)
#配置主题功能
xadmin.site.register(views.BaseAdminView, BaseSettings)
#更改全局配置
xadmin.site.register(views.CommAdminView, GlobalSettings)

