# -*- coding: utf-8 -*-

from django.db import models
class Data(models.Model):
    param1 = models.CharField(u"参数1",max_length=10)
    param2 = models.CharField(u"参数2", max_length=10)
    result = models.CharField(u"结果",max_length=10)