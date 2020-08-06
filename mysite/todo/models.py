from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    date_created = models.DateTimeField()
    detail = models.TextField()

class UrgentItem(models.Model):
    content = models.TextField()
    date = models.DateField()
    
