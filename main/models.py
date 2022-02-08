from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=40)
    describtion=models.CharField(max_length=255)
    sent_at=models.DateTimeField(auto_now_add=True)
