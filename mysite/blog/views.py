from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Comment
from django.utils import timezone
from .forms import PostForm,CommentForm

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now(),published=True).order_by('created_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

@login_required
def post_draft(request):
    posts=Post.objects.filter(published=False).order_by('created_date')
    return render(request,'blog/post_draft.html',{'posts':posts})

@login_required
def post_publish(request,pk):
    post=Post.objects.get(pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def post_edit(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.created_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'blog/post_new.html',{'form':form})

@login_required
def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.created_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/post_new.html',{'form':form})

@login_required
def post_delete(request,pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form=UserCreationForm()
        return render(request,'blog/register.html',{'form':form})

def comment_new(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comm=form.save(commit=False)
            comm.post=post
            comm.created_date=timezone.now()
            comm.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comments.html',{'form':form})
