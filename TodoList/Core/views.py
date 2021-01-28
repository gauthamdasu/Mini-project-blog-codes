from django.shortcuts import render
from django.http import HttpResponse

from .models import todo

def index(request):
    list_todo = todo.objects.filter(status=False)
    return render(request, 'base.html', {'list_todo': list_todo})

def mark_as_done(request, id):
    obj = todo.objects.get(pk=id)
    obj.status = True
    obj.save()
    list_todo = todo.objects.filter(status=False)
    return render(request, 'base.html', {'list_todo': list_todo})

def new_todo(request):
    if request.method == "POST":
        print(request.POST)
        todo.objects.create(name=request.POST.get('todo-name'))
        list_todo = todo.objects.filter(status=False)
        return render(request, 'base.html', {'list_todo': list_todo})
