from django.shortcuts import render,redirect,get_object_or_404
from  django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.

@login_required
def add_task(request):
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.owner=request.user
            task.save()
            messages.success(request,'Task added!')
            return redirect('task_list')
    else:
        form=TaskForm()
    return render(request,'tasks/add_task.html',{'form':form})

@login_required
def task_list(request):
    tasks=Task.objects.filter(owner=request.user).order_by('-created_at')
    return render(request,'tasks/task_list.html',{'tasks':tasks})

@login_required
def edit_task(request,pk):
    task=get_object_or_404(Task,pk=pk,owner=request.user)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Task updated!')
            return redirect('task_list')
    else:
        form=TaskForm(instance=task)
    return render(request,'tasks/edit_task.html',{'form':form})

@login_required
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk,owner=request.user)
    if request.method=='POST':
        task.delete()
        messages.success(request,'Task deleted!')
        return redirect('task_list')
    return render(request,'tasks/delete_task.html',{'task':task})

@login_required
@require_POST
def toogle_task(request,pk):
    task=get_object_or_404(Task,pk=pk,owner=request.user)
    task.is_done=not task.is_done
    task.save()
    messages.success(request,'Task status changed!')
    return redirect('task_list')

