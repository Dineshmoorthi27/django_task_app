from django.shortcuts import render,redirect
from taskmanager.models import Task , Screenshot
from taskmanager.forms import TaskForm,EditTaskForm,DescriptionForm
from django.core.paginator import Paginator
# Create your views here.
def task_list(request,):
    if request.method == "POST":
        form = TaskForm(request.POST,request.FILES)
        if form.is_valid():
            task =form.save()
            if request.FILES.get('screenshot'):
                Screenshot.objects.create(task=task, image=request.FILES['screenshot'])
            return redirect('task_list')
    else:
        tasks = Task.objects.all()
        paginator=Paginator(tasks,5)
        page_number = request.GET.get('pg')
        tasks=paginator.get_page(page_number)
        form = TaskForm()
    context = {
        'alltasks': tasks,
        'form':form
    }
    return render(request, 'task/task_list.html', context)

def edit_task(request,id=0):
    data = Task.objects.get(id=id)
    form = EditTaskForm(instance=data)
    screenshots = data.screenshots.all()
    if request.method == "POST":
        form = EditTaskForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            task = form.save()
            if request.FILES.get('screenshot'):
                Screenshot.objects.create(task=task, image=request.FILES['screenshot'])
            return redirect('task_list')        
    return render(request,"task/edit_task.html",{'form':form, 'screenshots': screenshots})
def delete_Task(request,id=0):
    data = Task.objects.get(id=id)
    data.delete()
    return redirect('task_list')
def task_description(request,id=0):
    data = Task.objects.get(id=id)
    description_form=DescriptionForm(instance=data)
    screenshots = data.screenshots.all()
    return render(request,"task/task_description.html",{'form':description_form,'screenshots': screenshots})




