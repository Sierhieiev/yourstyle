# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('news.views',
    # indexes
    url(r'^$', views.IndexView.as_view(), name='index'),
    #category
    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoriesView.as_view(), name='category'),
    #post
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostView.as_view(), name='post'),
    #Label
    url(r'^label/(?P<slug>[-\w]+)/$', views.LabelView.as_view(), name='label'),
    #arhiv
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive', name='archive'),
    )
