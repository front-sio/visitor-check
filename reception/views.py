from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from nida import load_user
from customer.models import Customer, License, Passport
from office.models import Office
from visitor.models import Visitor
import json
from django.http import JsonResponse
from visitor.forms import saveVisitorForm
from django.utils import timezone
from datetime import timedelta
from django.db import models
from avocado.decorators import customer_only, allowed_user, reception_only



@login_required
@reception_only
def reception_dashboard(request):
    office = Office.objects.all()
    data = {
        'offices': office,
    }
    return render(request, 'reception/dashboard/index.html', data)

@login_required
@reception_only
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
@reception_only
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

