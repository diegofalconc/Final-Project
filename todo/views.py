from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'todo/index.html')

def tasks(request):
    task_list=Task.objects.all()
    return render(request, 'todo/todolist.html', {'task_list': task_list})

def about(request):
    return render(request, 'todo/about.html')


@login_required
def taskdetail(request, id):
    task=get_object_or_404(Task, pk=id)
    context={
        'task' : task,
    }
    return render(request, 'todo/taskdetail.html', context=context)

@login_required
def newTask(request):
     form=TaskForm
     if request.method=='POST':
          form=TaskForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TaskForm()
     else:
          form=TaskForm()
     return render(request, 'todo/newTask.html', {'form': form})

@login_required
def delete(request, id):

    task=get_object_or_404(Task, pk=id)
    context={
        'task' : task,
    }
    Task.objects.filter(id=id).delete()
    return render(request, 'todo/delete.html', context=context)


def loginmessage(request):
    return render(request, 'todo/loginmessage.html')

def logoutmessage(request):
    return render(request, 'todo/logoutmessage.html')