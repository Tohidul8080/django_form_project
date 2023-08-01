from django import forms
from datetime import date
from django.core import validators


def even_or_not(value):
    if value%2 == 1:
        raise forms.ValidationError("please insert an even Number")
class user_form(forms.Form):
   # name=forms.CharField(validators=[validators.MaxLengthValidator(10)])

# arguments (required=False,initial="yourname", label="First Name")
#,widget=forms.TextInput(attrs={'placeholder':"enter your name"})
# , widget=forms.TextInput(attrs={'type':'date','type':'width:100px'})
    user_name=forms.CharField(required=False, label="First Name", widget=forms.TextInput(attrs={'placeholder':'Enter your name', 'style':'width:300px'}) )

    user_email=forms.EmailField(required=False,label="First Gmail", widget=forms.TextInput(attrs={'placeholder':'enter your email'}))
   # user_id=forms.IntegerField(label="First Id")
    user_id=forms.IntegerField(validators=[even_or_not,validators.MaxValueValidator(10),validators.MinValueValidator(4)])
    user_dob=forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={'type':'date'}))
    comment = forms.CharField(widget=forms.Textarea)
    boolean_fiel=forms.BooleanField(required=False)
    char_field=forms.CharField(max_length=20, min_length=4)
    #char_field1=forms.CharField(label="Char Field")
    #choices=(
            #  ( ' ','--Selected--' ),
             # (1,'CSE'),
              #(2,'EEE'),
              #(3,'CIVIL'),

    #)
    #argument choices=choices
    #choice_field=forms.choiceField(choices=choices)
    choice_field=forms.MultipleChoiceField(choices=((' ', '--selected --'),(1,'CSE'),(2,'EEE'),(3,'CIVIL')), required=False)
    choices=(('A','A'),('B','B'),('C','C'))
   # radio_field=forms.MultipleChoiceField(choices=choices, )
   # radio_field=forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    radio_field=forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)
    
