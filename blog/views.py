from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    qs=Post.objects.all()

    q=request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    response = render(request, 'blog/post_list.html',{
        'post_list': qs,
        'q': q,
    })
    # HttpResponse 인스턴스인데, render를 통해서, 좀 더 쉽게 템플릿을 통한 렌더링
    response
    return response


def post_detail(request, id):
    # try:
    #     post=Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html',{
        'post':post,
    })