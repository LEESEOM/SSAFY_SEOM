from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if thing in product_price:
        price = product_price[thing]*cnt
    else:
        price = -1
    context = {
        'price' : price,
        'thing' : thing ,
        'cnt' : cnt
    }
    return render(request, 'prices/price.html', context)