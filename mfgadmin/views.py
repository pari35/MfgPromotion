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
from .forms import Promotion


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
@api_view(['POST','GET'])

def promotion(request):
    if request.method=="POST":
        Promotions_title=request.POST.get("promotion_title")
        product=request.POST.get("product")
        retail_barcode=request.POST.get("retail_barcode")
        Mcode=request.POST.get("m_code")
        status=request.POST.get("status")
        available_for=request.POST.get("avl")
        start_date=request.POST.get("s_date")
        end_date=request.POST.get("e_date")
        price=request.POST.get("price")
        quantity=request.POST.get("qty")
        Promotions(
            retail_barcode=retail_barcode,
            Promotions_title=Promotions_title,
            product=product,
            Mcode=Mcode,
            status=status,
            available_for=available_for,
            start_date=start_date,
            end_date=end_date,
            price=price,
            quantity=quantity,
        ).save()
             
    def __str__(self):
        return str(self.Promotions_title)

    return render(request,'promotion.html')

def assign_promo(request):
    return render(request,'Assign_promo.html')

def nav_bar(request):
    return render(request,'nav.html')

def assign_promo_image(request):
    pic=request.FILES['image']
    from .models import assign_promo_image
    image=assign_promo_image(pic=pic)
    image.save()
    return render(request,'assign-promo.html')