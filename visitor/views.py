from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from nida import load_user
from customer.models import Customer, License, Passport
from office.models import Office
from visitor.models import Visitor
import json
from django.http import JsonResponse
from .forms import saveVisitorForm
from django.utils import timezone
from datetime import timedelta
from django.db import models
from avocado.decorators import customer_only, allowed_user


@login_required
@customer_only
def dashboard(request):
    now = timezone.now()
    offices = Office.objects.all().order_by('-created_on')[:8]
    visitors = Visitor.objects.all()
    # result = Office.objects.aggregate(
    #     total=models.Count('id'),
    #     today=models.Count('id', filter=models.Q(created_on__date=now.date())),
    #     yesterday=models.Count('id', filter=models.Q(created_on__date__gte=(now - timedelta(hours=24)).date())),
    #     last_7_day=models.Count('id', filter=models.Q(created_on__date__gte=(now - timedelta(days=7)).date())),
    # )
    data = {
        'offices': offices,
        'visitors': visitors,
        }
    return render(request, 'visitors/index.html', data)


@login_required
def saveForm(request):
    form = saveVisitorForm()
    if request.method == "POST":
        form = saveVisitorForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('visitors')
    return render(request, 'visitors/visitor/form.html', {'form': form})


@login_required
def visitors_view(request):
    visitors = Visitor.objects.all()
    data = {
        'visitors': visitors,
        }
    return render(request, 'visitors/visitor/index.html', data)


@login_required
def search_form(request, pk):
    office = Office.objects.get(id = pk)
    data = {
        'office': office,
    }
    return render(request, 'visitors/visitor/search_form.html', data)

@login_required
@allowed_user
def search_office_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('national_id')

        offices = Office.objects.filter(name=name)
        data = {
            'office'
        }
        return JsonResponse({'data': data})

@login_required
def search_view(request):
    data = {}
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # national_id = json.loads(request.body).get('national_id')
        id_number = request.POST.get('id_number')
        vd = load_user(national_id=id_number, json = True)
        print(vd)
        if vd == id_number:
            data = []
            item = {
                'NIN': vd.NIN,
                'FirstName': vd.FirstName,
                'MiddleName': vd.MiddleName,
                'LastName': vd.LastName,
                'DateofBirth': vd.DateofBirth,
                'Sex': vd.Sex,
            
            }
            data.append(item)
            res = data
            print(data)
            return JsonResponse({'data': res})
        # license user check condition
        elif id_number == License.objects.filter(id_number__icontains=id_number):
            vd = License.objects.filter(id_number__icontains=id_number)
            for pos in vd:
                data = []
                item = {
                    'NIN': pos.id_number,
                    'FirstName': pos.FirstName,
                    'MiddleName': pos.MiddleName,
                    'LastName': pos.LastName,
                    'Sex': pos.Sex,
                }
                data.append(item)
                res = data
                print(data)
                return JsonResponse({'data': res})
        elif id_number == Passport.objects.filter(id_number__icontains=id_number):
            vd = Passport.objects.filter(id_number__icontains=id_number)
            for pos in vd:
                data = []
                item = {
                    'NIN': pos.id_number,
                    'FirstName': pos.FirstName,
                    'MiddleName': pos.MiddleName,
                    'LastName': pos.LastName,
                    'Sex': pos.Sex,
                
                }
                data.append(item)
                res = data
                print(data)
                return JsonResponse({'data': res})
        else:
            res = "Unknown visitor try another way"
        return JsonResponse({'data': res}) 
    return JsonResponse(({}))
    # return render(request, 'visitors/visitor/search.html', data)


@login_required
@allowed_user
def kyc(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        res = None
        id_number = request.POST.get('id_number')

        user_info = load_user(national_id=id_number)
        if user_info is not None:
            if id_number == user_info.get('Nin'):
                ui = load_user(national_id=id_number)
                # print(ui)
                data = []
                item = {
                    'NIN': ui.Nin,
                    'FirstName': ui.Firstname,
                    'MiddleName': ui.Middlename,
                    'LastName': ui.Surname,
                    'DateofBirth': ui.Dateofbirth,
                    'Sex': ui.Sex,
                }
                data.append(item)
                res = data
                # print(res)
        else:
            res = 'No data match!'
        return JsonResponse({'data': res})
        
    return JsonResponse({})

@login_required
@allowed_user
def save_visitor(request):
    form = saveVisitorForm()
    if request.method == "POST":
        form = saveVisitorForm(request.POST)
        first_name = request.POST.get('first_name')
        id_number = request.POST.get('id_number')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        on_behalf = request.POST.get('on_behalf')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        # visited_from = request.POST.get('visited_from')
        # date_visited = request.POST.get('date_visited')
        office_visited = request.POST.get('office_visited')

        save_visitor = Visitor(
            first_name=first_name, 
            id_number=id_number, 
            on_behalf=on_behalf, 
            last_name=last_name,
            middle_name=middle_name,
            gender=gender,
            date_of_birth=date_of_birth,
            # visited_from=visited_from,
            # date_visited=date_visited,
            office_visited=office_visited,
            )

        save_visitor.save()
        return JsonResponse({})
    return JsonResponse({})


# display office list on the visitor save form
@login_required
def visitor_form(request):
    office = Office.objects.all()
    data = {
        'office': office,
    }
    return render(request, 'visitors/visitor/add.html', data)


@login_required
@customer_only
def delete_visitor(request, pk):
    visitor = Visitor.objects.get(id = pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitors')
    context = {'visitor': visitor,'item': visitor}
    return render(request, 'visitors/visitor/delete.html', context)


@login_required
def delete_office(request, pk):
    office = Office.objects.get(id = pk)
    if request.method == 'POST':
        office.delete()
        return redirect('offices')
    context = {'office': office,'item': office}
    return render(request, 'visitors/office/delete.html', context)
