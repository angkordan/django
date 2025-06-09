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
        code = request.POST['code'].upper()
        if request.POST['user_package'] == 'basic':
            if code == 'TEMMY':
                return redirect('https://paystack.shop/pay/nuvia_basic-disc')
            else:
                return redirect('https://paystack.shop/pay/nuvia_basic')
        elif request.POST['user_package'] == 'premium':
            if code == 'TEMMY':
                return redirect('https://paystack.shop/pay/nuvia_premium-disc')
            else:
                return redirect('https://paystack.shop/pay/nuvia_Premium')

    return render(request, 'signup.html')


def signin(request):
    """Login page"""

    return render(request, 'login.html')


