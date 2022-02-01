from django import forms
from .models import Promotions,AssignPromotion


class Promotion(forms.ModelForm):
    class Meta:
        model =Promotions
        fields=['retail_barcode','Promotions_title','product','Mcode','status','available_for','start_date','end_date','price','quantity']
        # widgets = {
        #     'retail_barcode':forms.TextInput(attrs={'class':'form-control my-3','placeholder':'Enter employee name'}), 
        #     'Promotions_title': forms.Select(attrs={'class':'form-control my-3'}),
        #     'product':  forms.Select(attrs={'class':'form-control my-3'})            
        #     'Mcode':  forms.Select(attrs={'class':'form-control my-3'})            
        #     'status':  forms.Select(attrs={'class':'form-control my-3'})            
        #     'available_for':  forms.Select(attrs={'class':'form-control my-3'})            
        #     'start_date':  forms.Select(attrs={'class':'form-control my-3'})            
        #     'end_date':  forms.Select(attrs={'class':'form-control my-3'})            
        #     'price':  forms.Select(attrs={'class':'form-control my-3'})            
        #     'quantity':  forms.Select(attrs={'class':'form-control my-3'})            
        # }

class AssignPromo(forms.ModelForm):
    class Meta:
        model=AssignPromotion
        fields=['station_id','station_name','operation_region','region','area','promo_image']