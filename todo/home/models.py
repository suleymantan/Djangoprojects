from django.db import models

class ToDoList(models.Model):
   

    todo = models.CharField(max_length=200)
    todo_date = models.DateTimeField(auto_now_add=True )
    statu = models.BooleanField(default=False)
    commence = models.DateField(null=True)
    fin = models.DateField(null=True)

    def __str__(self):
        return f"{self.todo}"
