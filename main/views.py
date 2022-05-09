from django.shortcuts import render

EVENT_NAVBAR = {
    'Upcoming Events': '/upcoming',
    'Host Event': '/add-event',
    'Hosted Events': '/hosted'
}

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
        'navs': EVENT_NAVBAR
    }
    return render(request, 'upcoming_conferences.html', context)

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
    return render(request,'sign_up.html')

def add_event(request):
    context = {
        'title': 'Host Event',
        'navs': EVENT_NAVBAR,
        'active': 'Host Event'
    }

    return render(request, 'add_event.html', context=context)

def view_event(request):
    context = {
        'title': 'Event Details',
    }

    return render(request, 'view_event.html')