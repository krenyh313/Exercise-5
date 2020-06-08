from django.shortcuts import render, redirect, reverse

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html') 

def contact_form(request):
    return render(request, 'contact_form.php')