from django.shortcuts import render

from blog.models import Entry  # Reuse the model from the blog app

def home(request):
    # This is the same logic as blog/views.py, but used here
    entries = Entry.objects.all().order_by('title') 
    return render(request, "home.html", {"entries": entries})