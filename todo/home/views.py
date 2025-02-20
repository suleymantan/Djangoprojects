from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import TodoForm


def home(request):
    todo_list = ToDoList.objects.all()
    completed = ToDoList.objects.filter(statu = True).values()
    no_completed = ToDoList.objects.filter(statu = False).values()
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
     
    context = {
        "form" : form,
        "todo_list":todo_list,
        "completed":completed,
        "no_completed":no_completed
    }
        
    return render(request, "home.html",context)

def updateTask(request,id):
    todo = ToDoList.objects.get(id=id)
    
    if request.method =='POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)


    context = {'form':form}
    return render(request,"update.html",context)

def delete(request,id):
    todo = ToDoList.objects.get(id=id)
    if request.method =='POST':
        todo.delete()
        return redirect('home')
    
    return render(request, "delete.html",{'todo':todo})

def completed(request,id):
    todo = ToDoList.objects.get(id=id)
    
    if request.method =='POST':
        todo.statu = True
        todo.save()
        return redirect('home')
    return render(request, "completed.html",{'todo':todo})


