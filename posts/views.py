from django.shortcuts import render, redirect

from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import PostForm
# Create your views here.


@login_required(login_url='/account/')
def index(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(
        location_city=request.user.profile.city)
    userId = request.user.id
    return render(request, 'index.html',
                  {'userId': userId,
                   'posts': posts})


@login_required(login_url='/account/')
def CreatePost(request):
    if request.user.profile.city is not None and request.user.last_name is not '':
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.created_by = request.user
                form.instance.location_city = request.user.profile.city
                form.save()
                return redirect('/')
        context = {'form': form, 'stat': 'Add Post'}
        return render(request, 'create.html', context)
    else:
        messages.info(request, 'Please Update your location or Name')
        return redirect("profile")


@login_required(login_url='/login')
def updatePost(request, pk):
    Posts = Post.objects.get(id=pk)
    form = PostForm(instance=Posts)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=Posts)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'pk': pk,
               'stat': 'Update or Delete', 'type': 'gad'}
    return render(request, 'update.html', context)


@login_required(login_url='/login')
def deletePost(request, pk):
    Posts = Post.objects.get(id=pk)

    if request.method == "POST":

        Posts.delete()
        return redirect('/')
    context = {'item': Posts, 'pk': pk, 'type': 'gad'}
    return render(request, 'delete.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
