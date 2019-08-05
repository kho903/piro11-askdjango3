from django.urls import re_path

from . import views_cbv
from . import views

urlpatterns=[
    re_path(r'^$', views_cbv.post_list, name='post_list'),
    re_path(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),

    re_path(r'^new/$', views.post_new, name='post_new'),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),

    re_path(r'^cbv/new/$', views_cbv.post_new),
    re_path(r'^cbv/(?P<pk>\d)/edit/$', views_cbv.post_edit),
    re_path(r'^cbv/(?P<pk>\d)/delete/$', views_cbv.post_delete),
]