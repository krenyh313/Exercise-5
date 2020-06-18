from django.shortcuts import render, redirect, reverse
from .models import Message

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html') 

def contact_form(request):
    _name = request.GET['name']
    _email = request.GET['email']
    _subject = request.GET['subject']
    _message = request.GET['message']
    msg = Message(name = _name, email = _email, subject = _subject, message = _message)
    msg.save()
    return render(request, 'contact_form.html')