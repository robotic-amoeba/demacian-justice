from django.shortcuts import render

def index(request, _):
    return render(request, 'frontend/index.html')
