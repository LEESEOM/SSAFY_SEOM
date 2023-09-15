from django.shortcuts import render

# Create your views here.
def first(request):
    info = request.GET.get('info')
    context = {
        'info' : info
    }    
    return render(request, 'throw_catch/first.html', context)


def second(request):
    info = request.GET.get('info')
    context = {
        'info' : info
    }
    return render(request, 'throw_catch/second.html', context)