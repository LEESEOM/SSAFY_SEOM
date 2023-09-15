from django.shortcuts import render

import random

# Create your views here.
def first(request):
    message = request.GET.get('message')
    print(message)
    context = {
        'message' : message
    }
    return render(request, 'throw_loops/first.html', context)


def second(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'throw_loops/second.html', context)


def third(request):
    message = []
    message.append(request.GET.get('message1'))
    message.append(request.GET.get('message2'))
    msg = random.choice(message)
    context = {
        'message' : msg
    }
    return render(request, 'throw_loops/third.html', context)