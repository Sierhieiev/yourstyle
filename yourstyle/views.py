from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'text': "Hello world!",}
    return render(request, 'yourstyle/index.html', context)

