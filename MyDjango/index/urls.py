from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('login.html', loginView, name='login'),
]
