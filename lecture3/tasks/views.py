from django.shortcuts import render
tasks = [
    "Do laundry",
    "Write code",
    "Read a book",
]
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        task = request.POST.get("task")
        tasks.append(task)
    return render(request, 'tasks/add.html', {
        "tasks": tasks
    } )