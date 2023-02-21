from django.http import HttpResponse
from django.shortcuts import redirect


def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('customer_dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def allowed_user(allowed_role=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                wrapper_func(request, *args, **kwargs)
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator



def customer_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'office_admin'  and request.user.is_active:
            return redirect('office_dashboard')
        elif group == 'receptionist' and request.user.is_active:
            return redirect('rec_dashboard')
        elif request.user.is_staff and request.user.is_superuser and request.user.is_active:
            return redirect('admin_dashboard')
        elif group == 'customer' and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func




def staff_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer' and request.user.is_active:
            return redirect('customer_dashboard')
        elif group == 'receptionist' and request.user.is_active:
            return redirect('rec_dashboard')
        elif group == 'office_admin' and request.user.is_active:
            return redirect('off_dashboard')
        elif request.user.is_staff and request.user.is_superuser and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func


def office_staff_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer' and request.user.is_active:
            return redirect('customer_dashboard')
        elif group == 'receptionist' and request.user.is_active:
            return redirect('rec_dashboard')
        
        elif request.user.is_staff and request.user.is_superuser and request.user.is_active:
            return redirect('admin_dashboard')
        elif group == 'office_admin' and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func



def reception_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer' and request.user.is_active:
            return redirect('customer_dashboard')
        
        elif group == 'office_admin' and request.user.is_active:
            return redirect('off_dashboard')
        elif request.user.is_staff and request.user.is_superuser and request.user.is_active:
            return redirect('admin_dashboard')

        elif group == 'receptionist' and request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func