"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
#from django.urls import path,include

#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('core.urls'), name='core'),
# ]
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns =[
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^dojo/', include('dojo.urls')),
    url(r'^shop/', include('shop.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/',include(debug_toolbar.urls)),
    ]
