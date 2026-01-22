from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Task.objects.create(content=content)
        return redirect('/')

    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})
