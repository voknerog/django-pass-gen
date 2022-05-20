from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    length = int(request.GET.get('length'))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+'))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def info(request):
    return render(request, 'generator/info.html')
