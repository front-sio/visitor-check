from django.shortcuts import render, redirect
from .models import Customer, Receptionist
from django.contrib.auth.models import Group
from .forms import receptionist_form, save_customer_form, CustomerForm
from django.http import JsonResponse




def save_customer(request):
    if request.method== "POST":
        form = save_customer_form(request.POST)
        form.username = request.POST.get('username')
        form.password1 = request.POST.get('password1')
        form.password2 = request.POST.get('password2')
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='vendor')
            user.groups.add(group)
            Customer.objects.create(user = user, display_name = user.username)
            return JsonResponse({})
    return JsonResponse({})


def customerUpdate(request, pk):
    customer = Customer.objects.get(id = pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('admin_customers')
    context = {
        'form': form
    }
    return render(request, 'avocado/customers/update.html', context)



def save_receptionist(request):
    form = receptionist_form()
    if request.method== "POST":
        form = receptionist_form(request.POST)
        form.username = request.POST.get('username')
        form.first_name = request.POST.get('first_name')
        form.last_name = request.POST.get('last_name')
        form.email = request.POST.get('email')
        form.password1 = request.POST.get('password1')
        form.password2 = request.POST.get('password2')
        customer = request.user.customer
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='receptionist')
            user.groups.add(group)
            Receptionist.objects.create(
            user = user,
            name = user.username,
            customer=customer
            )
            return redirect("home")
