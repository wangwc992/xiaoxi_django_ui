from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'aiClient.html')


def stream(request):
    return render(request, 'stream.html')


def stream1(request):
    return render(request, 'stream1.html')
