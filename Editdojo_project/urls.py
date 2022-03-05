from django.contrib import admin
from django.urls import path
from todo.views import todoView, addItem, deleteItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todoView),
    path('addTodo/', addItem),
    path('deleteTodo/<int:todo_id>', deleteItem)
]
