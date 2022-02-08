from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from main.models import Todo

# Create your views here.

# получение данных из Бд

def main(request):
    todos = Todo.objects.all()
    return render(request,'index2.html',{'todos':todos})

def error(request):
    todo=Todo.objects.all()
    return render(request,'erroe.html')


def create(request):
    if request.method == 'POST':
        todo=Todo()
        todo.title = request.POST.get("title")
        todo.describtion = request.POST.get("describtion")
        # send.sent_at = request.POST.get("")
        
        todo.save()
    return HttpResponseRedirect('/')


# def delete(request,id):
#     try:

#         todo = Todo.objects.get(id=id)
#         # todo.delete()
#         todo.save()
#         return HttpResponseRedirect('/')
#     except Todo.DoesNotExist:
#         return render(request,'erroe.html')

def test(request,id):
    todos2=Todo.objects.all()
    # todo=Todo.objects.get(id=id)
    return render(request,'index2.html',{'todos2':todos2, 'hello':'hello','id':id})



def test(request,id):
    todo=Todo.objects.get(id=id)
    print(todo)
    return render(request,'index2.html',{'todo':todo})

def delete(request,id):
    try:
        todo = Todo.objects.get(id=id)
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.describtion = request.POST.get('describtion')
            todo.save()
            return HttpResponseRedirect('/')
        return render(request, 'edit.html',{'todo':todo})
    except Todo.DoesNotExist:
        return render(request,'erroe.html')
        


def edit(request,id):
    try:
        todo = Todo.objects.get(id=id)
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.describtion = request.POST.get('describtion')
            todo.save()
            return HttpResponseRedirect('/')
        return render(request, 'edit.html',{'todo':todo})
    except Todo.DoesNotExist:
        return render(request,'erroe.html')

# def edit (request,id):
#     todo=Todo.objects.all()
#     return(request,'edit.html')   

def tasks(request):
    todos=Todo.objects.all()
    return render(request, 'tasks.html',{'todos':todos})
