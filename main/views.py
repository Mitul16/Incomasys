from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def upcoming_conferences(request):
    return render(request, 'upcoming_conferences.html')