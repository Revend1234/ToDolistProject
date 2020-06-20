from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    Todotitle=models.CharField(max_length=255)
    Todotext=models.TextField()
    Todocreatedate=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Todotitle
    
    class Meta:
        db_table='Todo'
        verbose_name_plural='Todos'

