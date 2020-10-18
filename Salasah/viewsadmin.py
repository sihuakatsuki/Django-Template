from django.shortcuts import render

def home(request):
    return render(request, 'Backend/Home/home.html')
