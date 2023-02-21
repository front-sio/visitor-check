from django.shortcuts import render, redirect
from .models import Office
from django.http import JsonResponse




def offices_view(request):
    offices = Office.objects.all().order_by('-created_on')[:10]
    print(offices)
    data = {
        'offices': offices,
    }
    return render(request, 'visitors/offices/index.html', data)

def office_form(request):
    return render(request, 'visitors/offices/office_forms.html')

def delete_office(request, pk):
    office = Office.objects.get(id = pk)
    if request.method == 'POST':
        office.delete()
        return redirect('offices')
    context = {'office': office,'item': office}
    return render(request, 'visitors/offices/delete.html', context)


def save_office(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        name = request.POST.get('name')
        created_on = request.POST.get('created_on')

        save_your_office = Office.objects.create(name=name, created_on=created_on)
        save_your_office.save()

        new_office = Office.objects.all().order_by('-created_on')

        if len(new_office) > 0:
            data = []
            for pos in new_office:
                item = {
                    'pk': pos.pk,
                    'name': pos.name,
                    'created_on': pos.created_on,
                }

                data.append(item)
                res = data
        return JsonResponse({'data': res})
    return JsonResponse({})
