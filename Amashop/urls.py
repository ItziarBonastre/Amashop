"""Amashop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from mybaskets.views import *
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^logout/$', log_out),
    url(r'^login/$', 'django.contrib.auth.views.login'),

    url('^register/', CreateView.as_view(template_name='registration/register.html', form_class=UserCreationForm, success_url='/')),

    url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mybaskets/', include('mybaskets.urls', namespace='mybaskets')),
)
