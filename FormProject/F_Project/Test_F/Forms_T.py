from django import forms
from django.core import validators
from Test_F import models

class model_form(forms.ModelForm):
    class Meta:
        model=models.F_table
        fields="__all__"


    

