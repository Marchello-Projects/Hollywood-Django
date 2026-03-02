import re
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import PatientRecord

User = get_user_model()

def validate_ukrainian_phone(phone):
    if not phone:
        return phone
    
    phone = re.sub(r'[^0-9+]', '', phone)
    
    if phone.startswith('0'):
        phone = '+38' + phone
    elif phone.startswith('380'):
        phone = '+' + phone
        
    if not re.match(r'^\+380\d{9}$', phone):
        raise ValidationError("Введіть коректний номер у форматі +380XXXXXXXXX")
        
    return phone

def validate_ukrainian_full_name(full_name):
    if not full_name:
        return full_name
    
    full_name = full_name.strip()
    
    pattern = r"^[А-ЩЬЮЯҐЄІЇа-щьюяґєії\'\-]+\s+[А-ЩЬЮЯҐЄІЇа-щьюяґєії\'\-]+(\s+[А-ЩЬЮЯҐЄІЇа-щьюяґєії\'\-]+)?$"
    
    if not re.match(pattern, full_name):
        raise ValidationError("Введіть повне ПІБ українською мовою (мінімум 2 слова).")
        
    return full_name


class BookingForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = [
            'full_name', 
            'phone', 
            'email', 
            'is_adult', 
            'visit_reason', 
            'clinic_address'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Іванов Іван Іванович'
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'placeholder': '+380XXXXXXXXX'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@gmail.com'
            })
        }

    def clean_phone(self):
        return validate_ukrainian_phone(self.cleaned_data.get('phone'))

    def clean_full_name(self):
        return validate_ukrainian_full_name(self.cleaned_data.get('full_name'))


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль", 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введіть пароль'
        })
    )
    password_confirm = forms.CharField(
        label="Підтвердження пароля", 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторіть пароль'
        })
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone']
        labels = {
            'full_name': 'ПІБ',
            'email': 'Електронна пошта',
            'phone': 'Номер телефону',
        }
        widgets = {
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'placeholder': '+380XXXXXXXXX'
            }),
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Іванов Іван Іванович'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@gmail.com'
            })
        }

    def clean_phone(self):
        return validate_ukrainian_phone(self.cleaned_data.get('phone'))

    def clean_full_name(self):
        return validate_ukrainian_full_name(self.cleaned_data.get('full_name'))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Паролі не співпадають.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@gmail.com'
        })
    )
    password = forms.CharField(
        label="Пароль", 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введіть пароль'
        })
    )