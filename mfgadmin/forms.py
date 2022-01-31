from django import forms
from .models import Promotions,AssignPromotion


class Promotion(forms.ModelForm):
    class Meta:
        model =Promotions
        fields=['retail_barcode','Promotions_title','product','Mcode','status','available_for','start_date','end_date','price','quantity']
        

class AssignPromo(forms.ModelForm):
    class Meta:
        model=AssignPromotion
        fields=['station_id','station_name','operation_region','region','area','promo_image']