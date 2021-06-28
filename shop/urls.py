from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about_us, name="about"),
    path('contact-us/', views.contact_us, name="contact_us"),
]
