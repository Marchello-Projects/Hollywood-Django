from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import BookingForm, RegistrationForm, LoginForm
from .models import PatientRecord

def home_page(request):
    return render(request, 'index.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('patient_profile')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_profile')
    else:
        form = RegistrationForm()
        
    return render(request, 'Hollywood/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('patient_profile')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('patient_profile')
            else:
                form.add_error(None, 'Невірна електронна пошта або пароль.')
    else:
        form = LoginForm()
        
    return render(request, 'Hollywood/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            if request.user.is_authenticated:
                record.user = request.user
            record.save()
            messages.success(request, 'Ваш запис успішно створено! Очікуйте на дзвінок.')
            return redirect('book_appointment') 
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'full_name': request.user.full_name,
                'phone': request.user.phone,
                'email': request.user.email,
            }
        form = BookingForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'Hollywood/booking.html', context)


@login_required(login_url='/login/')
def patient_profile(request):
    records = PatientRecord.objects.filter(user=request.user).select_related('clinic_address')
    context = {
        'records': records,
        'user_info': request.user
    }
    return render(request, 'Hollywood/profile.html', context)