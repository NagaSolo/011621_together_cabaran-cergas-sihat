from django.shortcuts import render

from .models import Post
def rumah(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'landing/home.html', context)

def tentang(request):
    return render(request, 'landing/about.html', {'title': 'About'})