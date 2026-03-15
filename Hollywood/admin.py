from django.contrib import admin
from django.db import models
from django import forms
from unfold.admin import ModelAdmin
from .models import User, ClinicAddress, PatientRecord

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('email', 'full_name', 'phone', 'is_staff')
    search_fields = ('email', 'full_name', 'phone')
    list_filter = ('is_staff', 'is_superuser')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональні дані', {'fields': ('full_name', 'phone')}),
        ('Права доступу', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Дати', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(ClinicAddress)
class ClinicAddressAdmin(ModelAdmin):
    list_display = ('address',)
    search_fields = ('address',)

@admin.register(PatientRecord)
class PatientRecordAdmin(ModelAdmin):
    list_display = ('full_name', 'phone', 'clinic_address', 'visit_reason', 'status', 'visit_date')
    list_filter = ('status', 'clinic_address', 'visit_reason')
    search_fields = ('full_name', 'email', 'phone')
    date_hierarchy = 'visit_date'
    list_editable = ('status', 'visit_date')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    def get_changelist_form(self, request, **kwargs):
        kwargs.setdefault('form', forms.ModelForm)
        return super().get_changelist_form(request, **kwargs)

    formfield_overrides = {
        models.DateTimeField: {
            "form_class": forms.DateTimeField,
            "widget": forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M', 
                attrs={
                    'type': 'datetime-local',
                    'step': '1800',
                    'class': 'border border-gray-200 dark:border-gray-700 text-gray-900 dark:text-gray-300 rounded-md px-2 py-1 bg-transparent w-full',
                    'style': 'color-scheme: dark; min-width: 200px;'
                }
            ),
        },
    }