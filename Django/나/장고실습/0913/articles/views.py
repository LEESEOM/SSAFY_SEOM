from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def catch(request, name, num):
    context = {
        'name' : name,
        'num':num,
    }
    return render(request, 'articles/catch.html', context)