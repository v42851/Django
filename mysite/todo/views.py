# Todo and amazing Project
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, UrgentItem
from django.utils import timezone
from django.views import generic


def todo(request):
  all_todo_items = TodoItem.objects.all()
  all_urgent_items = UrgentItem.objects.all()
  context = {'todo': all_todo_items, 'urgent': all_urgent_items}
  return render(request, 'todo/todo.html', context)
	
def addTodo(request):
  #create a new todo all_items, save and redirect the browser
  new_item = TodoItem(content = request.POST['content'], detail = request.POST['detail'], date = request.POST['date'], date_created = timezone.now())
  new_item.save()
  return HttpResponseRedirect('/todo')

def deleteTodo(request, todo_id):
  #create a new todo all_items, save and redirect the browser
  delete_item = TodoItem.objects.get(id=todo_id)
  delete_item.delete()
  return HttpResponseRedirect('/todo')

class TodoContentView(generic.DetailView):
  model = TodoItem
  template_name = 'todo/content.html'
