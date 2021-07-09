from django.forms import ModelForm
from django import forms
from .models import Order

class OrderForm(ModelForm):
    OPTIONS = (
        ('Placed', 'Placed'),
        ('Processed', 'Processed'),
        ('Delivered', 'Delivered')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS, widget=forms.RadioSelect)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','amount','order_status']