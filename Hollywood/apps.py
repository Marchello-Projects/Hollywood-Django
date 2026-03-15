import os

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from dotenv import load_dotenv

load_dotenv()


class HollywoodConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Hollywood"

    def ready(self):
        post_migrate.connect(create_default_superuser, sender=self)


def create_default_superuser(sender, **kwargs):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    ADMIN_EMAIL = os.getenv("DJANGO_SUPERUSER_EMAIL")
    ADMIN_PASSWORD = os.getenv("DJANGO_SUPERUSER_PASSWORD")

    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        return

    if not User.objects.filter(email=ADMIN_EMAIL).exists():
        print(f"Creating superuser: {ADMIN_EMAIL}...")
        try:
            User.objects.create_superuser(email=ADMIN_EMAIL, password=ADMIN_PASSWORD)
            print("Superuser created successfully!")
        except Exception as e:
            print(f"Error creating superuser: {e}")
    else:
        print("Superuser already exists. Skipping creation.")
