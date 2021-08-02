from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(settings)  # 添加菜单模板
admin.site.register(setting_details)  # 添加菜单详情


