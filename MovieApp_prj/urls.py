"""MovieApp_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from magazines import views as magazine_views
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts import views as accounts_views
from Hello import views as hello_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello_views.get_index, name='index'),
    url(r'^subscribe/$', accounts_views.register, name='register'),
    url(r'^magazines/$', magazine_views.all_magazines),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
]
