from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def upcoming_conferences(request):
    return render(request, 'upcoming_conferences.html')

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')