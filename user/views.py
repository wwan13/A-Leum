from django.shortcuts import render,redirect
from django.contrib import auth
from .models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password'],
                gender=request.POST['gender'],
                age=request.POST['age'],
                phone=request.POST['phone'])
            auth.login(request, user)
            return redirect('login')
    return render(request, 'valunteer.html')