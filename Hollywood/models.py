from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class ClientStatus(models.TextChoices):
    COMPLETED_CONSULTATION = "COMPLETED", _("Консультацію проведено")
    WAITING = "WAITING", _("В очікуванні")

class ClinicAddress(models.Model):
    address = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = _("Адреса клініки")
        verbose_name_plural = _("Адреси клінік")

    def __str__(self):
        return self.address

class Patient(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True, db_index=True)
    
    is_adult = models.BooleanField(default=True)
    visit_reason = models.CharField(max_length=255, null=True, blank=True)
    visit_date = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    
    status = models.CharField(
        max_length=20,
        choices=ClientStatus.choices,
        default=ClientStatus.WAITING
    )

    clinic_address = models.ForeignKey(
        ClinicAddress,
        on_delete=models.PROTECT,
        related_name="patients",
        null=True, 
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'full_name']

    class Meta:
        verbose_name = _("Пацієнт")
        verbose_name_plural = _("Пацієнти")

    def __str__(self):
        return self.full_name or self.email