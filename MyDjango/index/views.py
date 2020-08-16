#视图文件，处理业务逻辑
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    print("aaa")
    print("fff")
    return render(request,"index.html")