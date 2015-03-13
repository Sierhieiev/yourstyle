from django.shortcuts import render
from django.conf import settings

def home(request):
    local = settings.LOCAL_USER_SETTINGS
    context = {
        'text': 'Hello world!',
        'site_title': local['site_title'],
        'site_short_description': local['site_short_description']
    }
    return render(request, 'yourstyle/index.html', context)

