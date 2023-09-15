from django.shortcuts import render

# Create your views here.
def calculator(request, num1, num2):
    sub = num1 - num2
    mul = num1 * num2
    if num2 != 0:
        div = num1 / num2
    else:
        div = False
    context = {
        'num1': num1,
        'num2':num2,
        'sub' : sub,
        'mul' : mul,
        'div' : div,
    }
    return render(request, 'calculators/calculator.html', context)