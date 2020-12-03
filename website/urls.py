from django.urls import path
from .views import home, contact, about, services, appointment
app_name = 'website'
urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('appointment/', appointment, name='appointment'),
]
