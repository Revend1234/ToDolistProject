from django.shortcuts import render
from .models import Todo
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'todoapp/index.html')

def gettodos(request):
    todos_list=Todo.objects.all()
    return render(request, 'todoapp/todos.html' ,{'todos_list' : todos_list})

def todosdetails(request, id):
    todos=get_object_or_404(Todo, pk=id)
    context={
        'todos' : todos,
    }
    return render(request, 'todoapp/todosdetails.html', context=context)   

@login_required
def newtodo(request):
     form=TodoForm
     if request.method=='POST':
          form=TodoForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TodoForm()
     else:
          form=TodoForm()
     return render(request, 'todoapp/newtodo.html', {'form': form})

def loginmessage(request):
    return render(request, 'todoapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'todoapp/logoutmessage.html')