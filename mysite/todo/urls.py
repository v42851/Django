from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todo, name='todo'),
    path('addTodo', views.addTodo),
    path('deleteTodo/<int:todo_id>', views.deleteTodo),
    path('<int:todo_id>', views.TodoContent)
]
