from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'navs': {
            'SIGN IN': '/sign-in',
            'REGISTER': '/sign-up'
        }
    }
    return render(request, 'home.html', context)

def upcoming_conferences(request):
    context = {
        'title': 'Dashboard',
        'navs': {
            'Upcoming': '/upcoming',
            'Hosted Events': '#'
        }
    }
    return render(request, 'upcoming_conferences.html', context)

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')