# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('news.views',
     # indexes
    url(r'^$', views.IndexView.as_view(), name='index'),
    #category
    url(r'^category/(?P<slug>[-\w]+)/$', 'category', name='category'),
    #post
    url(r'^post/(?P<slug>[-\w]+)/$', 'post', name='post'),
    #Label
     url(r'^category/(?P<slug>[-\w]+)/$', 'category', name='category'),
    )
