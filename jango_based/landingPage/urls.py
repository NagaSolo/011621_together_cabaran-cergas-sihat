from django.urls import path

from . import views

urlpatterns = [
    path('', views.rumah, name='landing-rumah'),
    path('tentang/', views.tentang, name='landing-tentang'),
]
