from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'shop/index.html')


def about_us(request):
    return render(request, 'shop/about.html')


def contact_us(request):
    return render(request, 'shop/contact_us.html')
