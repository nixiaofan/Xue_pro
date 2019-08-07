from django.db import models
from datetime import datetime
# from users.models import
# Create your models here.

class UserAsk(models.Model):
    '''用户提交的资讯信息'''
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    course_name = models.CharField(max_length=30, verbose_name='课程')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

# class CourseComments(models.Model):
