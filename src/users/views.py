from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) 
                messages.success(request, f'You are now logged in as {username} ')
                return redirect('home')
            else:
                messages.error(request, f'Unable to login.')
        else:
                messages.error(request, f'Unable to login.')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request,'views/login.html', {'login_form': login_form})

