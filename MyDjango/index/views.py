from django.shortcuts import render

def index(request):
    # 使用method属性判断请求方式
    if request.method == 'GET':
        # 类方法的使用
        print(request.is_secure())
        print(request.is_ajax())
        print(request.get_host())
        print(request.get_full_path())
        print(request.get_raw_uri())
        # 属性的使用
        print(request.COOKIES)
        print(request.content_type)
        print(request.content_params)
        print(request.scheme)
        # 获取GET请求的请求参数
        print(request.GET.get('user', ''))
        return render(request, 'index.html')
    elif request.method == 'POST':
        # 获取POST请求的请求参数
        print(request.POST.get('user', ''))
        return render(request, 'index.html')
