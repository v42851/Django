from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.utils import timezone
# Create your views here.

def todo(request):
  all_todo_items = TodoItem.objects.all()
  return render(request, 'todo/todo.html', {'all_items':all_todo_items})
	
def addTodo(request):
  #create a new todo all_items, save and redirect the browser
  new_item = TodoItem(content = request.POST['content'], date = request.POST['date'], date_created = timezone.now())
  new_item.save()
  return HttpResponseRedirect('/todo')

def deleteTodo(request, todo_id):
  #create a new todo all_items, save and redirect the browser
  delete_item = TodoItem.objects.get(id=todo_id)
  delete_item.delete()
  return HttpResponseRedirect('/todo')

def TodoContent(request, todo_id):
  todo_item = TodoItem.objects.get(id=todo_id)
  return render(request, 'todo/content.html', {'items':todo_item})