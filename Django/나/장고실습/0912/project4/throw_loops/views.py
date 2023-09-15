from django.shortcuts import render

# Create your views here.
def first(request, one):
    context = {

    }
    return render(request, 'throw_loops/first.html', context)

