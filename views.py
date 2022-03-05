from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(req):
    all_todo_items = TodoItem.objects.all()
    return render(req, 'todo.html', {
        'all_items': all_todo_items
    })

def addItem(req):
    # Retrieve post data
    # Add data to TodoItem object
    # Save TodoItem object
    new_item = TodoItem(content = req.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteItem(req, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo/')
