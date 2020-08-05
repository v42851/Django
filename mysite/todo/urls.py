from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todo, name='todo'),
    path('addTodo', views.addTodo, name = 'addtodo'),
    path('deleteTodo/<int:todo_id>', views.deleteTodo, name = 'deletetodo'),
    path('<int:pk>', views.TodoContentView.as_view(), name = 'content')
]
