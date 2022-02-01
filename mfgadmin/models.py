from django.db import models
from django.db.models import Model


# Create your models here.
class Promotions(models.Model):
    retail_barcode=models.IntegerField()
    Promotions_title=models.CharField(max_length=30)
    product=models.CharField(max_length=30)
    Mcode=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    available_for=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()
    price=models.IntegerField()
    quantity=models.IntegerField()

#model for assign new promo
class AssignPromotion(models.Model):
    station_id = models.BigAutoField(primary_key=True)
    station_name=models.CharField(max_length=50, null=True)
    operation_region=models.CharField(max_length=20)
    region=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    promo_image=models.ImageField(null=True,blank=True,upload_to="images/")

# @action(detail=True,methods=['POST'])