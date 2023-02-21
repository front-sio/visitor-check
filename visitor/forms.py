from django import forms


class saveVisitorForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
    middle_name = forms.CharField(label='middle name', max_length=100)
    gender = forms.CharField(label='gender', max_length=100)
    visited_from = forms.CharField(label='visited from', max_length=100)
    date_of_birth = forms.CharField(label='date of birth', max_length=100)
    id_number = forms.CharField(label='id number', max_length=20)
    on_behalf = forms.CharField(label='on behalf', max_length=200)
    office_visited = forms.CharField(label='office visited', max_length=100)