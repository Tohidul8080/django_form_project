from django.urls import path
from . import views

urlpatterns=[
    path('',views.contact_f,name='contact_f'),
    
]