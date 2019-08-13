# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-12 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('p', '培训机构'), ('g', '个人'), ('x', '高校')], default='p', max_length=20),
        ),
    ]