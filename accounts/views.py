from django.shortcuts import render, redirect
from customer.forms import save_customer_form
from avocado.decorators import authenticated_user
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

@authenticated_user
def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else: 
            messages.info(request, 'Username or password is incorrect!')
            
    context ={}
    return render(request, 'avocado/accounts/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')