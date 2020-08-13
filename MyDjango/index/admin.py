from django.contrib import admin
from .models import *

admin.site.site_title = 'MyDjango后台管理'
admin.site.site_header = 'MyDjango'


@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'name', 'age']


@admin.register(Vocation)
class VocationAdmin(admin.ModelAdmin):
    # 在数据列表页设置显示的模型字段
    list_display = ['id', 'job', 'title', 'payment']
