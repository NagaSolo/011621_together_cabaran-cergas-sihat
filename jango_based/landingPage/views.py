from django.shortcuts import render
from django.http import HttpResponse

def rumah(request):
    return render(request, 'landing/home.html')

def tentang(request):
    return render(request, 'landing/about.html', {'title': 'About'})