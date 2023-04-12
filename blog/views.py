from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.
# Routing for the urls

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')

# Remove???
# def blog(request):
#    return render(request, 'blog/blog.html')