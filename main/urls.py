from django.urls import path 

 
from .import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('addtodo/',views.addtodo,name="addtodo"),
    path('todolist/',views.todolist,name="todolist"),
    path('delete_todo/<int:todo_id>',views.delete,name="delete"),
    path('update_todo/<int:todo_id>',views.update,name="update"),
    path('Mark_Complete/<int:todo_id>',views.complete,name="complete"),
]
