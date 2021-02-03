from django.shortcuts import render
from django.http import HttpResponse

def rumah(request):
    return HttpResponse('<h1> Selamat datang Keluargaku Abe Din</h1>')