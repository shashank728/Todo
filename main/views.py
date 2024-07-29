from django.shortcuts import render,redirect

from .models import Todo
# Create your views here.


# ============================================ HOME ================================================
def home(request):
    return render(request,"home.html")


# ========================================== ADD TODO ===============================================
def addtodo(request):
    if request.method =="POST":
        
        # templates se views me aa gye 
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        # 
        new_todo = Todo(task = user_task , created_at = user_created_at)
        new_todo.save()
        
        return redirect("todolist")
    
    return render(request,"add_todo.html")


# ============================================= TODO LIST ==========================================


def todolist(request):
    todos = Todo.objects.all()
    
    incomplete_todos = [todo for todo in todos if todo.is_completed is not True]

    
    completed_todos = [todo for todo in todos if todo not in incomplete_todos ]

    
    parameter = {
        
        "todos" : incomplete_todos,
        "completed_todos": completed_todos
    }
    
    return render(request,"todo.html",parameter)



# ============================================= delete ==================================


def delete(reuqest, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect("todolist")

# ============================================== update ==================================

def update(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    
    parameter = {
        "todo" : todo
    }
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        todo.task = user_task
        todo.created_at = user_created_at
        
        todo.save()
        return redirect("todolist")
        
        
    return render(request,"todo_update.html",parameter)

# ======================================== complete task ===============================================


def complete(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.is_completed = True
    todo.save()
    return redirect("todolist")