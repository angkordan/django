from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    """Home page"""

    return render(request, 'index.html')


def signup(request):
    """Signup page"""

    if request.method =="POST":
        """Configure form submit action"""
        if request.POST['user_package'] == 'basic':
            if request.POST['code'] == 'TEMMY':
                return redirect('https://paystack.shop/pay/nuvia_basic-dis')
            elif request.POST['code'] != 'TEMMY':
                messages.info(request, 'Invalid Code')
                return redirect('signup')
            else:
                return redirect('https://paystack.shop/pay/nuvia_Basic')
        elif request.POST['user_package'] == 'premium':
            if request.POST['code'] == 'TEMMY':
                return redirect('https://paystack.shop/pay/nuvia_Prem-dis')
            elif request.POST['code'] != 'TEMMY':
                messages.info(request, 'Invalid Code')
                return redirect('signup')
            else:
                return redirect('https://paystack.shop/pay/nuvia_Premium')

    return render(request, 'signup.html')


def signin(request):
    """Login page"""

    return render(request, 'login.html')


