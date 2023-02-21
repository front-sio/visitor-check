
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from customer.models import Customer


class save_customer_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email','password1', 'password2']
    

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user',]





class receptionist_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name', 'email','password1', 'password2']