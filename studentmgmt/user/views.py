from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponseForbidden

def security_login(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and (user.is_security or user.is_superuser):
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid credentials or not a security user.'
    return render(request, 'user/login.html', {'error': error})
