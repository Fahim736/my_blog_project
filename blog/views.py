from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import BlogPost
from .forms import UserRegistrationForm, BlogPostForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('home')



def home_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def my_posts_view(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})

@login_required
def edit_post_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    if post.author != request.user:
        raise PermissionDenied("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit'})

@login_required
def delete_post_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    # Ownership authorization check
    if post.author != request.user:
        raise PermissionDenied("You are not allowed to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('my_posts')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
