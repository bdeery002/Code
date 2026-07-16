from django.shortcuts import render

def home(request):
    # Instead of rendering a 'home.html', just send them to the SOX index
    return render(request, "home.html")