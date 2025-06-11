# -*- coding: utf-8 -*-
import django
from .views import get_ueditor_controller

DJANGO_VERSION = django.VERSION[:2]

# Django 4.0+ 使用 path/re_path
if DJANGO_VERSION >= (4, 0):
    from django.urls import re_path
    urlpatterns = [
        re_path(r'^controller/$', get_ueditor_controller)
    ]

# Django 1.8 到 3.2 保持原逻辑
elif DJANGO_VERSION >= (1, 8):
    from django.conf.urls import url
    urlpatterns = [
        url(r'^controller/$', get_ueditor_controller)
    ]

# 移除Django 1.8以下的兼容代码（不再支持）
else:
    # 现代Django版本不再需要此分支
    urlpatterns = []