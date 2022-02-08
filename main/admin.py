from django.contrib import admin
from main.models import Todo
# Register your models here.




class TodoAdmin(admin.ModelAdmin):
    list_display = ("id","title","describtion","sent_at")

admin.site.register(Todo, TodoAdmin)