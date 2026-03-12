from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'), 
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('profile/', views.patient_profile, name='patient_profile'),
    path('quick-booking/', views.quick_book, name='quick_book'),
]