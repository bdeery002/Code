from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task", max_length=100)
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    # Sort the tasks list by the 'priority' key
    # reverse=True puts the highest numbers (5) at the top
    sorted_tasks = sorted(request.session["tasks"], key=lambda x: x['priority'], reverse=True)
    
    return render(request, 'tasks/index.html', {
        "tasks": sorted_tasks
    })

# Using Django Forms
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            
            # 1. Check if the session list exists, if not, create it
            if "tasks" not in request.session:
                request.session["tasks"] = []
            
            # 2. Append the new task to the session list
            # Note: We create a copy, modify it, then save it back
            tasks_list = request.session["tasks"]
            tasks_list.append({"name": task, "priority": priority})
            request.session["tasks"] = tasks_list

            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

def delete_all(request):
    if request.method == "POST":
        # Clear the session list
        request.session["tasks"] = []
        return HttpResponseRedirect(reverse("tasks:index"))
    
    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })