from django import forms


class saveOfficeForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)