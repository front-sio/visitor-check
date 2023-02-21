from django.shortcuts import render, redirect
from customer.forms import receptionist_form, save_customer_form
from django.contrib.auth import login, logout, authenticate
from avocado.decorators import staff_only
from customer.models import Customer
from visitor.models import Visitor
from office.models import Office
# Create your views here.



@staff_only
def avocado_dashboard(request):
    customer_count = Customer.objects.all().count()
    visitor_count = Visitor.objects.all().count()
    office_count = Office.objects.all().count()
    data = {
        'cust_total': customer_count,
        'vis_total': visitor_count,
        'offi_total': office_count,
    }
    return render(request, 'avocado/ds/index.html', data)

def avocado_customers(request):
    customers = Customer.objects.all()[:10]
    customer_count = Customer.objects.all().count()
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    data = {
        'customers': customers,
        'customer_total': customer_count,
    }
    return render(request, 'avocado/customers/index.html', data)



def avocado_visitors(request):
    visitor_count=Visitor.objects.all().count()
    visitors=Visitor.objects.all()
    data = {
        'visi_total': visitor_count,
        'visitors': visitors,
    }
    return render(request, 'avocado/visitors/index.html', data)



def avocado_offices(request):
    offices = Office.objects.all()
    office_count = Office.objects.all().count()

    data = {
        'offices': offices,
        'offi_total': office_count,
    }
    return render(request, 'avocado/offices/index.html', data)


def customer_form(request):
    form = save_customer_form()

    context = {
         'form': form
     }
    return render(request, 'avocado/customers/add.html', context)



def delete_customer(request, pk):
    customer = Customer.objects.get(id = pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')
    context = {'customer': customer,'item': customer}
    return render(request, 'avocado/customers/delete.html', context)


def delete_visitor(request, pk):
    visitor = Visitor.objects.get(id = pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitors')
    context = {'visitor': visitor,'item': visitor}
    return render(request, 'avocado/visitors/delete.html', context)


def delete_office(request, pk):
    office = Office.objects.get(id = pk)
    if request.method == 'POST':
        office.delete()
        return redirect('offices')
    context = {'office': office,'item': office}
    return render(request, 'avocado/offices/delete.html', context)


def customers_view(request):
    customers = Customer.objects.all().order_by('-created_on')[:12]
    context = {
        'customers': customers
    }
    return render(request, 'avocado/customers/index.html', context)


