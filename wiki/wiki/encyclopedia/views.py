from markdown2 import Markdown  
from django.shortcuts import render, redirect

from . import util

# Convert markdown content to HTML
def convert_med_to_html(title):
    entry_content = util.get_entry(title)
    markdowner = Markdown()
    if entry_content is not None:
        return markdowner.convert(entry_content)
    else:
        return None
    
# View for the index page
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    # Get the list of all entry names (e.g., ['CSS', 'Django', 'HTML'])
    entries = util.list_entries()
    
    # Check if the title exists in the list (ignoring case)
    # We look for a match where both are lowercase
    match = next((e for e in entries if e.lower() == title.lower()), None)

    if match:
        # If we found a match (like 'CSS' for 'css'), use the REAL filename
        html_content = convert_med_to_html(match)
        return render(request, "encyclopedia/entry.html", {
            "title": match,
            "content": html_content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested entry was not found."
        })
    

# View for search functionality

def search(request):
    query = request.GET.get('q', '').strip()
    all_entries = util.list_entries()

    # Case 1: Direct Match
    for entry in all_entries:
        if query.lower() == entry.lower():
            return redirect("entry", title=entry)

    # Case 2: Substring Match
    # This says: "Keep the entry if the query is INSIDE the entry name"
    results = [entry for entry in all_entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search_results.html", {
        "results": results,
        "query": query
    })