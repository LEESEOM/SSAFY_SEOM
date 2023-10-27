from django.shortcuts import render, get_list_or_404
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DepositOptions,DepositProducts
import requests
from django.http import JsonResponse
from .serializer import DepositProductsSerializer, DepositOptionsSerializer
from rest_framework import status
from django.db.models import Max 

# Create your views here.



@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    for li in response.get('result').get('baseList'):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li2 in response.get('result').get('optionList'):
        product_tmp = DepositProducts.objects.get(fin_prdt_cd=li2['fin_prdt_cd'])
        save_data2 = {
            'fin_prdt_cd' : li2.get('fin_prdt_cd'), 
            'intr_rate_type_nm' : li2.get('intr_rate_type_nm'), 
            'intr_rate' : li2.get('intr_rate'), 
            'intr_rate2' : li2.get('intr_rate2'), 
            'save_trm' : li2.get('save_trm'), 
        }
        
        if not li2.get('intr_rate'):
            save_data2['intr_rate'] = -1
        
        serializer = DepositOptionsSerializer(data=save_data2)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product_tmp)

    return Response({'message':'okay'})
           


@api_view(['GET','POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def deposit_product_options(request,fin_prdt_cd):
    deposit_options = get_list_or_404(DepositOptions,fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(deposit_options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    obj = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
    option = DepositOptions.objects.get(intr_rate2=obj['intr_rate2'])
    product = option.product
    serializer = DepositProductsSerializer(product)
    serializer2 = DepositOptionsSerializer(option)
    data = {
        'deposit_product' : serializer.data,
        'options' : serializer2.data
    }
    return Response(data)