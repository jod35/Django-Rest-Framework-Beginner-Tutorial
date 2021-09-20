from django.db import models

# Create your models here.



"""
    class Todo
        content:str
        priority:str choices=['low','medium','high']
        done:bool

"""


class Todo(models.Model):
    PRIORITIES=(
        ('LOW','low'),
        ('MEDIUM','medium'),
        ('HIGH','high'),
    )


    content=models.CharField(max_length=400)
    priority=models.CharField(max_length=10,choices=PRIORITIES)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.content