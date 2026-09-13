from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout 
from django.urls import reverse
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'spc/login.html')
    return render(request, 'spc/index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Perform authentication logic here (e.g., check against a database)
        if username == 'admin' and password == 'password':
            # Authentication successful, redirect to the index page
            return render(request, 'spc/index.html')
        else:
            # Authentication failed, show an error message
            return render(request, 'spc/login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'spc/login.html')