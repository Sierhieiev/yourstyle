from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'yourstyle.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace = 'news')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
