from markdown2 import Markdown  
from django.shortcuts import render, redirect
import random

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


# View for creating a new encyclopedia entry
def new_entry(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()

        # Check if entry already exists
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "An entry with this title already exists!"
            })
        
        # Save the new entry
        util.save_entry(title, content)
        
        # Redirect the user to the newly created page
        return redirect("entry", title=title)

    # If request is GET, just show the form
    return render(request, "encyclopedia/new_entry.html")

# View for editing an existing encyclopedia entry
def edit_entry(request, title):
    if request.method == "POST":
        # Get the updated content from the textarea
        content = request.POST.get("content")
        
        # Save the updated content (util.save_entry overwrites existing files)
        util.save_entry(title, content)
        
        # Redirect back to the entry's main page
        return redirect("entry", title=title)

    # If GET, fetch existing content to pre-populate the textarea
    content = util.get_entry(title)
    
    return render(request, "encyclopedia/edit_entry.html", {
        "title": title,
        "content": content
    })


def random_page(request):
    # 1. Get the list of all entry names
    entries = util.list_entries()
    
    # 2. Randomly select one title from the list
    selected_page = random.choice(entries)
    
    # 3. Redirect to the existing 'entry' view using that title
    return redirect("entry", title=selected_page)