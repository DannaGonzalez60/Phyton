from django.shortcuts import render

def index(request):
    return render (request, 'index.html', {
        'variable' : 'producto',
        'pro1' : 'loro'
    })

def contact(request):
    return render(request, 'contact.html', {
        
    })