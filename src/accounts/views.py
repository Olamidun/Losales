from django.shortcuts import render, HttpResponse
from .forms import UserRegistrationForm
from .models import Account
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password == password2 and len(password) > 6:
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email)
                user.set_password(password)
                user.save()
                return HttpResponse('User hasa been created successfully')
            elif password != password2:
                return HttpResponse('Passwords do not match, please try again')
            elif len(password) < 6:
                return HttpResponse('Password must be greater than 6 characters')
    else: 
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})   


# def login_view(request):
#     if request.
#     email = request.POST.get('email')
#     password = request.POST.get('password1')
#     user = authenticate(request, email=email, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponse(f'{user.last_name}, you have logged in successfully')
#     else:
#         return HttpResponse('Invalid credentials')