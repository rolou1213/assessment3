from django.forms import ModelForm
from .models import Widget
from django import forms 

class WidgetForm(forms.Form):
    
    description = forms.CharField(max_length=100)
    quantity = forms.IntegerField()