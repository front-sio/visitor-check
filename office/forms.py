
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from office.models import Office

class saveOfficeForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)



class save_office_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    

class OfficeUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Office
        fields = '__all__'
        exclude = ['user',]
