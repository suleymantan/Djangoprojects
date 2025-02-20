from django.contrib import admin
from .models import ToDoList


admin.site.register(ToDoList)
class AdminTodolist(admin.ModelAdmin):
    
    list_display = ("todo","todo_date","start_date","finish_date","statu")
    fields = ["todo","todo_date","start_date","finish_date","statu"]

