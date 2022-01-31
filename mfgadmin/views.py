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
from .forms import Promotions


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
        promo=Promotions(request.POST) 
        if promo.is_valid:
            promo.save()      
    return render(request,'promotion.html')

def assign_promo(request):
    return render(request,'Assign_promo.html')