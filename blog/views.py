from django.shortcuts import render

# Create your views here.
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋, 매소드
    return render(request, 'home.html', {'blogs' : blogs})

def about(request):
    return render(request, 'about.html')

def new(request):
    return render(request, 'new.html')