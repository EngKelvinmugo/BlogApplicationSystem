

from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    AllBlogs=Blogs.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)

def likeBlog(request,pk):
    blog=Blogs.objects.get(id=pk)
    blog.likes+=1
    blog.save()
    return redirect('/')