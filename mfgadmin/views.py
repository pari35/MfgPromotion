from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from pint import Quantity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sqlalchemy import false
from .models import Promotions
from .serializers import PromotionSerializer
from rest_framework.decorators import api_view
from .serializers import PromotionSerializer


# Create your views here.
@api_view(['GET'])
def api(request):
    return JsonResponse("api base",safe=True)

@api_view(['POST'])
def promotions(request):
    promo=Promotions.objects.all()
    serializer=PromotionSerializer(promo,many=True)
    return JsonResponse(serializer.data,safe=False)

#view for promotion tab
def promotion(request):
    if request.method=="POST":
        retail_barcode=request.POST['retail_barcode']
        Promotions_title=request.POST['promotion_title']
        product=request.POST['product']
        Mcode=request.POST['m_code']
        status=request.POST['status']
        available_for=request.POST['avl']
        start_date=request.POST['s_date']
        end_date=request.POST['e_date']
        price=request.POST['price']
        quantity=request.POST['qty']
        Promotions(retail_barcode=retail_barcode,Promotions_title=Promotions_title,product=product,Mcode=Mcode,status=status,available_for=available_for,start_date=start_date,end_date=end_date,price=price,quantity=quantity).save()
        
    return render(request,'promotion.html')

def assign_promo(request):
    return render(request,'Assign_promo.html')