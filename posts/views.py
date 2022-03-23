from django.shortcuts import render, redirect

from json import dumps
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import PostForm
import django_filters
# Create your views here.


@login_required(login_url='/login')
def index(request):
    user_data = list(User.objects.values())
    post_data = Post.objects.filter(
        location_city=request.user.profile.city)
    post_data = list(post_data.values())
    post_dataJSON = dumps(post_data)
    userId = request.user.id

    userget = request.user.first_name + " " + request.user.last_name
    return render(request, 'index.html', {'userId': userId, 'gdata': post_dataJSON, 'user': userget, 'user_data': user_data})


@login_required(login_url='/login')
def CreatePost(request):
    if request.user.profile.city is not None:
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.created_by = request.user
                form.instance.created_by_name = request.user.first_name + " " + request.user.last_name
                form.instance.location_city = request.user.profile.city
                form.save()
                return redirect('/youser/')
        context = {'form': form, 'stat': 'Add Post'}
        return render(request, 'create.html', context)
    else:
        messages.info(request, 'Please Update your location')
        return redirect("profile")


@login_required(login_url='/login')
def updatePost(request, pk):
    Posts = Post.objects.get(id=pk)
    form = PostForm(instance=Posts)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=Posts)
        if form.is_valid():
            form.save()
            return redirect('/youser/')
    context = {'form': form, 'pk': pk,
               'stat': 'Update or Delete', 'type': 'gad'}
    return render(request, 'update.html', context)


@login_required(login_url='/login')
def deletePost(request, pk):
    Posts = Post.objects.get(id=pk)

    if request.method == "POST":

        Posts.delete()
        return redirect('/youser/')
    context = {'item': Posts, 'pk': pk, 'type': 'gad'}
    return render(request, 'delete.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
