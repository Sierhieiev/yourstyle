from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'yourstyle.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace = 'news')),
)
