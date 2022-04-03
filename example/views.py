from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'hello': 'Hello'
    }
    return render(request, 'index.html', context)