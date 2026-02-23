from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

class PatientManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Поле Email обов\'язкове'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class ClientStatus(models.TextChoices):
    COMPLETED_CONSULTATION = "COMPLETED", _("Консультацію проведено")
    WAITING = "WAITING", _("В очікуванні")
    CANCELLED = "CANCELLED", _("Скасовано")

class ClinicAddress(models.Model):
    address = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = _("Адреса клініки")
        verbose_name_plural = _("Адреси клінік")

    def __str__(self):
        return self.address

class Patient(AbstractUser):
    username = None 
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True, db_index=True)
    
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="Вік")
    
    favorite_clinic = models.ForeignKey(
        ClinicAddress,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="frequent_patients",
        verbose_name="Часта поліклініка"
    )

    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'full_name']

    objects = PatientManager()

    class Meta:
        verbose_name = _("Пацієнт")
        verbose_name_plural = _("Пацієнти")

    def __str__(self):
        return self.full_name or self.email
        
    @property
    def is_adult(self):
        if self.age is not None:
            return self.age >= 18
        return True

class Visit(models.Model):
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name="visits",
        null=True, 
        blank=True
    )
    
    guest_name = models.CharField(max_length=100, null=True, blank=True)
    guest_phone = models.CharField(max_length=20, null=True, blank=True)
    
    reason = models.CharField(max_length=255, verbose_name="Причина візиту")
    date = models.DateTimeField(verbose_name="Дата візиту")
    clinic = models.ForeignKey(
        ClinicAddress, 
        on_delete=models.PROTECT, 
        related_name="visits"
    )
    status = models.CharField(
        max_length=20,
        choices=ClientStatus.choices,
        default=ClientStatus.WAITING
    )
    
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("Візит")
        verbose_name_plural = _("Візити")
        ordering = ['-date']

    def __str__(self):
        name = self.patient.full_name if self.patient else self.guest_name
        return f"Візит: {name} - {self.date.strftime('%d.%m.%Y')}"

@receiver(post_save, sender=Visit)
def update_favorite_clinic(sender, instance, created, **kwargs):
    if instance.patient:
        frequent_clinic_dict = instance.patient.visits.values('clinic').annotate(
            visit_count=Count('clinic')
        ).order_by('-visit_count').first()

        if frequent_clinic_dict:
            clinic_id = frequent_clinic_dict['clinic']
            if instance.patient.favorite_clinic_id != clinic_id:
                instance.patient.favorite_clinic_id = clinic_id
                instance.patient.save(update_fields=['favorite_clinic'])