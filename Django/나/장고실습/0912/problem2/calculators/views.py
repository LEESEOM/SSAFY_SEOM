from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'calculators/calculators.html')


def catch(request):
    print(request)
    print(request.GET)
    one = request.GET.get('one')
    two = request.GET.get('two')
    m = int(one)-int(two)
    x = int(one)*int(two)
    if two != '0':
        d = int(one)/int(two)
    else:
        d = '0'
    context = {
        'one' : one,
        'two' : two,
        'm' : m,
        'x' : x,
        'd' : d,
    }
    return render(request, 'calculators/result.html', context)