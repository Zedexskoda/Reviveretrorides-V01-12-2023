from django import forms
from .models import *
from crispy_forms.helper import FormHelper

class AllDetailForm(forms.ModelForm):
    class Meta:
        model = All_Detail
        fields = ['car', 'car_model', 'year', 'registration_no', 'chassis_no', 'engine_no', 'owner_name', 'manufacturing_year', 'state']


class CarXModForm(forms.ModelForm):
    class Meta:
        model = car_x_mod
        fields = ['car', 'work','before_work', 'estimate', 'remarks',]
      

class FinalSettlementForm(forms.ModelForm):
    class Meta:
        model = final_settlement
        fields = ['car', 'work', 'after_work', 'estimate', 'Final_cost', 'remarks']