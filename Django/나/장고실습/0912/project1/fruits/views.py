from django.shortcuts import render

# Create your views here.
def fruits(request):
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]
    context={
        'fruit_list' : fruit_list,
        'hate' : hate,
    }
    return render(request, 'fruits/fruits.html', context)

def index(request):
    menus = ['짜장면','짬뽕','마라탕','탕수육','족발']
    users = []
    context = {
        'menus' : menus,
        'users' : users
    }
    return render(request, 'fruits/index.html', context)