
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from . import models
from .forms import PostForm


def news(request):
    posts = models.Post.objects.all()
    print(posts)
    return render(request,'blog/news.html',{'posts': posts})

def add_news(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('news')  # Redirect to the news list page after submission
    else:
        form = PostForm()  # Create an empty form for GET requests

    return render(request, 'blog/add_post.html', {'form': form})
def edit_news(request, id):
    post = models.Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Bind form to the post instance
        if form.is_valid():
            form.save()  # Save the updated post
            return redirect('news')  # Redirect to the news list after saving
    else:
        form = PostForm(instance=post)  # Pre-fill form with the current post data

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
