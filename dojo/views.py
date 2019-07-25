import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post



def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            #방법2
            # post = Post(title=form.cleaned_data['title'],
            #             content=form.cleaned_data['content'])
            # post.save()

            #방법3
            # post = Post.objects.create(title=form.cleaned_data['title'],
            #                            content=form.cleaned_data['content'])
            #방법4
            post = form.save(commit = False)
            post.ip=request.META['REMOTE_ADDR']
            post.save()
            #post = Post.objects.create(**form.cleaned_data)
            return redirect('/dojo/') #namespace: name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })





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