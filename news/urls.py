# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news import views, feeds

urlpatterns = patterns('news.views',
    # indexes
    url(r'^$', views.GenericListView.as_view(), name='index'),
    #category
    url(r'^category/(?P<slug>[-\w]+)/$', views.GenericListView.as_view(), name='category'),
    #post
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostView.as_view(), name='post'),
    #Label
    url(r'^label/(?P<slug>[-\w]+)/$', views.GenericListView.as_view(), name='label'),
    #archive
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.ArchiveView.as_view(), name='archive'),
    #rss
    url(r'^rss/$', feeds.RssLatestPosts(), name='rss'),
    #atom
    url(r'^atom/$', feeds.AtomLatestPosts(), name='atom')
    )
