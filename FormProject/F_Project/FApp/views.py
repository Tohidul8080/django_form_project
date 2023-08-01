from django.shortcuts import render
from django.http import HttpResponse
from FApp import forms

# Create your views here.
def Home(request):
    diction={}
    return render(request, 'Home.html', context=diction)


def form(request):
    new_form=forms.user_form()
    diction={'text_form':new_form, 'heading1':'This form is created using django library'}

    if request.method == 'POST': # form submit hoice ki na check kore
        new_form=forms.user_form(request.POST)
        diction.update({'text_form':new_form})

        if new_form.is_valid():
            user_name=new_form.cleaned_data['user_name']
            user_email=new_form.cleaned_data['user_email']
            user_id=new_form.cleaned_data['user_id']
            user_dob=new_form.cleaned_data['user_dob']
            comment=new_form.cleaned_data['comment']
            boolean_fiel=new_form.cleaned_data['boolean_fiel']
            char_field=new_form.cleaned_data['char_field']
            choice_field=new_form.cleaned_data['choice_field']
            radio_field=new_form.cleaned_data['radio_field']
            #name=new_form.cleaned_data['name']
            
            diction.update({'user_name':user_name})
            diction.update({'user_email':user_email})
            diction.update({'user_id':user_id})
            diction.update({'user_dob':user_dob})
            diction.update({'comment':comment})
            diction.update({'boolean_fiel':boolean_fiel})
            diction.update({'char_field':char_field})
            diction.update({'choice_field':choice_field})
            diction.update({'radio_field':radio_field})
            #diction.update({'name':name})
           # diction.update({'char_field':new_form.cleaned_data['char_field']})
            diction.update({'A_B':'yes'})
           # diction.update({'form_submited':'Yes'})
           



    return render(request, 'form.html',context=diction)
