import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post


# class DetailView(object):
#     def __init__(self, model):
#         self.model = model
#
#     def get_object(self, *args, **kwargs):
#         return get_object_or_404(self.model, id=kwargs['id'])
#
#     def get_template_name(self):
#         return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)
#
#     def dispatch(self, request, *args, **kwargs):
#         return render(request, self.get_template_name(), {
#             self.model._meta.model_name: self.get_object(*args, **kwargs),
#         })
#
#     @classmethod
#     def as_view(cls, model):
#         def view(request, *args, **kwargs):
#             self = cls(model)
#             return self.dispatch(request, *args, **kwargs)
#         return view


post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')



# def generate_view_fn(model):
#     def view_fn(request, id):
#         instance = get_object_or_404(model,id=id)
#         instance_name = model._meta.model_name
#         template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
#         return render(request, template_name,{
#             instance_name: instance,
#         })
#     return view_fn




# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return render(request, 'dojo/post_detail.html',{
#         'post':post,
#     })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법2
            # post = Post(title=form.cleaned_data['title'],
            #             content=form.cleaned_data['content'])
            # post.save()

            # 방법3
            # post = Post.objects.create(title=form.cleaned_data['title'],
            #                            content=form.cleaned_data['content'])
            # 방법4
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            # post = Post.objects.create(**form.cleaned_data)
            return redirect('/dojo/')  # namespace: name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


def mysum(request, numbers):
    # request: HttpRequest
    # return HttpResponse(int(x)+int(y)+int(z))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = "지훈"
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>가나다라마바사아자차카타파하</p>
        '''.format(name=name))


def post_list2(request):
    name = '지훈'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬 장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = 'C:/dev/askdjango/gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')  # 'text/html'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
