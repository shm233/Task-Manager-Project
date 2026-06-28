from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myApp.models import *
from django.contrib.auth.decorators import login_required
from django.http import Http404

def signupPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        profile_pic = request.FILES.get('profile_pic')
        bio = request.POST.get('bio')
        
        if password==confirm_password:
            
            Custom_User.objects.create_user(
                username=username,
                password=password,
                email=email,
                profile_pic = profile_pic,
                bio = bio
                )
            messages.success(request, "Account created successfully.")
            return redirect("signinPage")

    return render(request, 'auth/signup.html')


def signinPage(request):

    if request.method == "POST":

        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)

        print(user)

        if user:
            login(request,user)
            return redirect("task_list")
        else:
            messages.warning(request, "User not found")
            
    return render(request,'auth/login.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('signinPage')

@login_required
def task_list(request):
    creator = request.user
    tasks = Task_Model.objects.filter(created_by = creator)
    context = {
        'tasks' : tasks
    }
    return render(request, 'task/task-list.html', context)

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        
        Task_Model.objects.create(
            title = title,
            description = description,
            due_date = due_date,
            priority = priority,
            status = status,
            created_by = request.user
        )
        messages.success(request, 'Data Added Successfully')
        return redirect('task_list')
    return render(request, 'task/add-task.html')

@login_required
def update_task(request, t_id):
    tasks = Task_Model.objects.get(id = t_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        
        tasks.title = title
        tasks.description = description
        tasks.due_date = due_date
        tasks.priority = priority
        tasks.status = status
        
        tasks.save()
        messages.success(request, 'Data Updated Successfully')
        return redirect(task_list)
    context = {
        'tasks' : tasks
    }
    return render(request, 'task/update-task.html', context)

@login_required
def delete_task(request, t_id):
    Task_Model.objects.get(id = t_id).delete()
    return redirect('task_list')
