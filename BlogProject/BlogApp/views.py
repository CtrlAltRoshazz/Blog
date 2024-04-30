from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import BlogModel
from . forms import BlogForm

from django.contrib import messages

# Create your views here.

def home_view(request):
    # return HttpResponse("Home Page")
    
    blogs = BlogModel.objects.all()
    context = {'blogs':blogs}
    
    return render(request , 'home.html', context)

def addblog_view(request):
    # return HttpResponse("Add Blog Page")
    
        # 1st method to add data into model
        # if request.method == 'POST':
        #     forms = BlogForm(request.POST)
        #     if forms.is_valid():
        #         forms.save()
        #         return redirect('home')            
        
        # 2nd method to add data into model
    if request.method == 'POST':
    
        title = request.POST['title']
        desc = request.POST['desc']
        
        blog = BlogModel(title = title , desc = desc)
        blog.save()
        messages.success(request , 'Blog Added Successfully')
        return redirect('home')
    
    
    forms = BlogForm()
    context = {'forms':forms}
    
    return render(request , 'addblog.html', context)

def dashboard_view(request):
    blogs = BlogModel.objects.all()
    context = {'blogs':blogs}
    
    return render(request, 'dashboard.html', context)

def updateblog_view(request, id):
    blog = BlogModel.objects.get(id = id)
    
    if request.method == 'POST':
        updated_title  = request.POST['update_title']
        updated_desc = request.POST['update_desc']
        
        blog.title = updated_title
        blog.desc = updated_desc
        
        blog.save()
        messages.success(request , 'Blog Updated Successfully')
        return redirect('home')
    
    
    context = {'blog' : blog}
    
    return render(request, 'updateblog.html', context)


def deleteblog_view(request , id):
    blog = BlogModel.objects.get(id = id)
    blog.delete()
    
    messages.warning(request , 'Blog Deleted Successfully')
    return redirect('home')
