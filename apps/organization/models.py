from datetime import datetime

from django.db import models

# Create your models here.
class CityDict(models.Model):
    '''城市'''
    name = models.CharField(max_length=50, verbose_name='城市名称')
    desc = models.TextField(verbose_name='城市描述')
    add_time = models.DateTimeField(datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='封面', max_length=100)
    address = models.CharField(max_length=100, verbose_name='机构地址')
    city = models.ForeignKey(CityDict, verbose_name='所在城市')
    category = models.CharField(max_length=20, choices=(('p', '培训机构'), ('g', '个人'), ('x', '高校')), default='p')

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师姓名')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    word_position = models.CharField(max_length=50, verbose_name='公司职位')
    points = models.CharField(max_length=50, verbose_name='教学特点')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name