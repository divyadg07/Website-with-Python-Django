from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable' : "this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This Is Home Page :-) ")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This Is About Page :-) ")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This Is Services Page :-) ")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        info = request.POST.get('info')
        contact = Contact(name=name, email=email, phone=phone, info=info, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')
    #return HttpResponse("This Is Contact Page :-) ")