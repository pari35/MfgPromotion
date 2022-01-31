from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from sqlalchemy import null

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
    quantity=models.IntegerField(default=null)

#model for assign new promo
class AssignPromotion(models.Model):
    station_id = models.BigAutoField(primary_key=True)
    station_name=models.CharField(max_length=50)
    operation_region=models.CharField(max_length=20)
    region=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
