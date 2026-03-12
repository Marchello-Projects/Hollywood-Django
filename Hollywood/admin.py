from django.contrib import admin
from .models import User, ClinicAddress, PatientRecord

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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
class ClinicAddressAdmin(admin.ModelAdmin):
    list_display = ('address',)
    search_fields = ('address',)

@admin.register(PatientRecord)
class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'clinic_address', 'visit_reason', 'status', 'visit_date')
    list_filter = ('status', 'clinic_address', 'visit_reason')
    search_fields = ('full_name', 'email', 'phone')
    date_hierarchy = 'visit_date'
    list_editable = ('status', 'visit_date')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)