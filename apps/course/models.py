from django.db import models

from organization.models import CourseOrg
# Create your models here.
class Course(models.Model):
    '''课程'''
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=100, verbose_name='描述')
    detail = models.TextField(verbose_name='详情')
    degree = models.CharField(max_length=10, choices=(('pri', '初级'), ('mid', '中级'), ('hig', '高级')))
    learn_times = models.IntegerField(verbose_name='学习时长', default=0)
    students = models.IntegerField(verbose_name='学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数', default=0)
    img = models.ImageField(upload_to='Course/%Y/%m', verbose_name='课程图片')
    click_nums = models.IntegerField(verbose_name='点击人数', default=0)
    add_time = models.DateTimeField(auto_now_add=True)
    org = models.ForeignKey(CourseOrg, verbose_name='机构', default='')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    '''章节'''
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=50, verbose_name='章节名')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    '''章节的视频'''
    lesson = models.ForeignKey('Lesson', verbose_name='视频')
    name = models.CharField(max_length=50, verbose_name='视频名')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    '''课程的资料'''
    course = models.ForeignKey('Course', verbose_name='课程')
    name = models.CharField(max_length=40, verbose_name='资料名')
    download = models.FileField(upload_to='Resource/%Y/%m', verbose_name='资料')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '资料'
        verbose_name_plural = verbose_name

