from django.urls import path

from blog import views_cbv
from . import views

urlpatterns=[
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path(r'^cbv/new/$', views_cbv.post_new),
]