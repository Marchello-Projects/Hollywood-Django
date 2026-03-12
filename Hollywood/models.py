from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class VisitReason(models.TextChoices):
    CONSULTATION = "consultation", "📋 Консультація"
    ACUTE_PAIN = "acute_pain", "⚡ Гострий біль"
    FILLING_LOST = "filling_lost", "🦷 Випала пломба"
    PROSTHETICS = "prosthetics", "🦷 Протезування"
    IMPLANTATION = "implantation", "🔩 Імплантація"
    
    HYGIENE_ADULT = "hygiene_adult", "✨ Чистка та Гігієна"
    THERAPY_ADULT = "therapy_adult", "🦷 Лікування (Пломба/Канали)"
    ORTHO_ADULT = "ortho_adult", "🔩 Протезування та Імплантація"
    SURGERY_ADULT = "surgery_adult", "💉 Видалення зуба"
    
    HYGIENE_CHILD = "hygiene_child", "✨ Чистка молочних зубів"
    THERAPY_CHILD = "therapy_child", "🧸 Пломба/Лікування молочного зуба"
    SURGERY_CHILD = "surgery_child", "🦷 Видалення молочного зуба"

class ClientStatus(models.TextChoices):
    WAITING = "waiting", "В очікуванні"
    COMPLETED = "completed", "Консультацію проведено"

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email обов'язковий"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Електронна пошта"), unique=True)
    full_name = models.CharField(_("ПІБ"), max_length=255, blank=True)
    phone = models.CharField(_("Номер телефону"), max_length=20, blank=True)
    
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class ClinicAddress(models.Model):
    CLINIC_CHOICES = [
        ('Овідіополь, Портова 13', 'Овідіополь, Портова 13'),
        ('Чорноморськ, проспект Миру 41', 'Чорноморськ, проспект Миру 41'),
    ]
    
    address = models.CharField(_("Адреса"), max_length=255, choices=CLINIC_CHOICES, unique=True)
    
    class Meta:
        verbose_name = "Адреса клініки"
        verbose_name_plural = "Адреси клінік"

    def __str__(self):
        return self.address

class PatientRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="records")
    email = models.EmailField(_("Електронна пошта"))
    full_name = models.CharField(_("ПІБ"), max_length=100)
    phone = models.CharField(_("Номер телефону"), max_length=20)
    
    visit_reason = models.CharField(
        _("Причина візиту"),
        max_length=50,
        choices=VisitReason.choices
    )
    
    clinic_address = models.ForeignKey(ClinicAddress, on_delete=models.PROTECT, verbose_name=_("Адреса поліклініки"))
    
    status = models.CharField(
        _("Статус"),
        max_length=20,
        choices=ClientStatus.choices,
        default=ClientStatus.WAITING
    )
    
    visit_date = models.DateTimeField(_("Дата візиту"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Запис"
        verbose_name_plural = "Записи"
        indexes = [models.Index(fields=['email'])]
        ordering = ['-visit_date']

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.get_visit_reason_display()}"