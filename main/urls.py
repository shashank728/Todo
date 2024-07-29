from django.urls import path 
from django.Conf.url.static import static
from django.conf. import settings 
from .import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('addtodo/',views.addtodo,name="addtodo"),
    path('todolist/',views.todolist,name="todolist"),
    path('delete_todo/<int:todo_id>',views.delete,name="delete"),
    path('update_todo/<int:todo_id>',views.update,name="update"),
    path('Mark_Complete/<int:todo_id>',views.complete,name="complete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
