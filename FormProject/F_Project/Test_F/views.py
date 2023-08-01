from django.shortcuts import render
from django.http import HttpResponse
from Test_F import Forms_T
from Test_F.models import F_table
from Test_F import Forms_T


# Create your views here.

def contact_f(request):
        First_List=F_table.objects.order_by('first_name')
        diction={'F_table':First_List}
 
        #diction.update({'user_vmail':validators_mail.cleaned_data['user_vmail']})
        return render(request,'Home.html',context=diction)

def form(request):
   
    new_form=Forms_T.model_form()  

    if request.method == "POST": 
          new_form=Forms_T.model_form(request.POST)
          if new_form.is_valid():
                new_form.save(commit=True)
                return contact_f(request)
          diction={'test_f':new_form,'heading_1':'Add new table'}
    return render(request, 'form.html',context=diction)