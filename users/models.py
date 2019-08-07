

from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class UserProfile(AbstractUser):
    '''user拓展'''
    nick_name = models.CharField(max_length=20, verbose_name='昵称')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=20, choices=(('male', '男'), ('female', '女')), default='female')
    address = models.CharField(max_length=50, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=120)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    '''邮箱验证'''
    code = models.CharField(max_length=20, verbose_name='验证码')
    mail = models.EmailField(max_length=40, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '忘记密码')), max_length=30)
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}+{1}".format(self.code, self.mail)


class PageBanner(models.Model):
    '''轮播图'''
    title = models.CharField(max_length=50, verbose_name='标题')
    img = models.ImageField(upload_to='banner/%Y/%m', verbose_name='图片')
    url = models.URLField(max_length=200, verbose_name='url地址')
    index = models.IntegerField(default=20, verbose_name='顺序号')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


