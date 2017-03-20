# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json
from home_application.models import Data

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def compute(request):
    param1 = int(request.GET.get('param1'))
    param2 = int(request.GET.get('param2'))
    result = param1 * param2
    Data.objects.create(
        param1=param1,
        param2=param2,
        result=result

    )
    return render_json({'result':result})