from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Office
from django.http import JsonResponse
from avocado.decorators import customer_only, allowed_user

from office.forms import save_office_form, OfficeUpdateForm


def offices_view(request):
    offices = Office.objects.all().order_by('-created_on')[:10]
    print(offices)
    data = {
        'offices': offices,
    }
    return render(request, 'visitors/offices/index.html', data)



@login_required
@customer_only
def office_form(request):
    customer = request.user.customer
    print(customer)
    return render(request, 'visitors/offices/office_forms.html')

def delete_office(request, pk):
    office = Office.objects.get(id = pk)
    if request.method == 'POST':
        office.delete()
        return redirect('offices')
    context = {'office': office,'item': office}
    return render(request, 'visitors/offices/delete.html', context)


# def save_office(request):
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':

#         name = request.POST.get('name')
#         created_on = request.POST.get('created_on')

#         save_your_office = Office.objects.create(name=name, created_on=created_on)
#         save_your_office.save()

#         new_office = Office.objects.all().order_by('-created_on')

#         if len(new_office) > 0:
#             data = []
#             for pos in new_office:
#                 item = {
#                     'pk': pos.pk,
#                     'name': pos.name,
#                     'created_on': pos.created_on,
#                 }

#                 data.append(item)
#                 res = data
#         return JsonResponse({'data': res})
#     return JsonResponse({})


def save_office(request):
    if request.method== "POST":
        customer = request.user.customer
        form = save_office_form(request.POST)
        form.username = request.POST.get('username')
        form.email = request.POST.get('email')
        form.first_name = request.POST.get('first_name')
        form.last_name = request.POST.get('last_name')
        form.password1 = request.POST.get('password1')
        form.password2 = request.POST.get('password2')
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='office_admin')
            user.groups.add(group)
            Office.objects.create(user = user, company=customer, name = user.username, first_name=user.first_name,last_name=user.last_name)
            return JsonResponse({})
    return JsonResponse({})


def officeUpdate(request, pk):
    office = Office.objects.get(id = pk)
    form = OfficeUpdateForm(instance=office)
    if request.method == "POST":
        form = form = OfficeUpdateForm(request.POST, instance=office)
        if form.is_valid():
            form.save()
            return redirect('admin_offices')
    context = {
        'form': form
    }
    return render(request, 'office/profile/update.html', context)