import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


# Create your views here.


def mysum(request, numbers):
    # request: HttpRequest
    #return HttpResponse(int(x)+int(y)+int(z))
    result=sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name ="지훈"
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>가나다라마바사아자차카타파하</p>
        '''.format(name=name))


def post_list2(request):
    name = '지훈'
    return render(request,'dojo/post_list.html', {'name': name })


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬 장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params = {'ensure_ascii': False})


def excel_download(request):
    # filepath = 'C:/dev/askdjango/gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # 'text/html'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response