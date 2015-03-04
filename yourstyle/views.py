from django.shortcuts import render


def home(request):
    context = {'text': "Hello world!",}
    return render(request, 'yourstyle/index.html', context)

