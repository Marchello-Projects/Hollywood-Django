from datetime import datetime, timedelta

from django.contrib import admin, messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render
from django.utils.timezone import now

from .forms import BookingForm, EditProfileForm, LoginForm, RegistrationForm
from .models import ClinicAddress, PatientRecord

User = get_user_model()


def home_page(request):
    return render(request, "index.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("patient_profile")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("patient_profile")
    else:
        form = RegistrationForm()

    return render(request, "Hollywood/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("admin:index")
        return redirect("patient_profile")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect("admin:index")
                return redirect("patient_profile")
            else:
                form.add_error(None, "Невірна електронна пошта або пароль.")
    else:
        form = LoginForm()

    return render(request, "Hollywood/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def book_appointment(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            if request.user.is_authenticated:
                record.user = request.user
            record.save()
            messages.success(
                request, "Ваш запис успішно створено! Очікуйте на дзвінок."
            )
            return redirect("patient_profile")
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                "full_name": request.user.full_name,
                "phone": request.user.phone,
                "email": request.user.email,
            }
        form = BookingForm(initial=initial_data)

    context = {"form": form}
    return render(request, "Hollywood/booking.html", context)


@login_required(login_url="/login/")
def patient_profile(request):
    records = PatientRecord.objects.filter(user=request.user).select_related(
        "clinic_address"
    )

    favorite_clinic = None
    if records.exists():
        fav_clinic_data = (
            records.values("clinic_address__address")
            .annotate(count=Count("clinic_address"))
            .order_by("-count")
            .first()
        )
        if fav_clinic_data:
            favorite_clinic = fav_clinic_data["clinic_address__address"]

    if request.method == "POST":
        if "edit_profile" in request.POST:
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Профіль успішно оновлено.")
                return redirect("patient_profile")
        elif "delete_account" in request.POST:
            user = request.user
            logout(request)
            user.delete()
            return redirect("home")
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        "records": records,
        "user_info": request.user,
        "favorite_clinic": favorite_clinic,
        "form": form,
    }
    return render(request, "Hollywood/profile.html", context)


def quick_book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Ваш запис успішно створено! Очікуйте на дзвінок."
            )
            return redirect("quick_book")
    else:
        form = BookingForm()

    return render(request, "Hollywood/quick_booking.html", {"form": form})


@staff_member_required
def registry_calendar_view(request):
    clinics = ClinicAddress.objects.all()

    time_slots = []
    start_time = datetime.strptime("08:00", "%H:%M")
    end_time = datetime.strptime("20:00", "%H:%M")

    while start_time <= end_time:
        time_slots.append(start_time.strftime("%H:%M"))
        start_time += timedelta(minutes=30)

    date_str = request.GET.get("date")
    if date_str:
        try:
            current_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            current_date = now().date()
    else:
        current_date = now().date()

    prev_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)

    records = PatientRecord.objects.filter(
        visit_date__date=current_date
    ).select_related("clinic_address")

    context = admin.site.each_context(request)
    context.update(
        {
            "clinics": clinics,
            "time_slots": time_slots,
            "records": records,
            "current_date": current_date,
            "prev_date": prev_date.strftime("%Y-%m-%d"),
            "next_date": next_date.strftime("%Y-%m-%d"),
        }
    )

    return render(request, "admin/registry_calendar.html", context)
