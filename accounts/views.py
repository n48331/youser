from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, City


def login(request):
    if request.method == 'POST' and "login_form":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userget = request.user.username
            auth.login(request, user)
            if request.user.profile.city is not None:
                return redirect("youser/")
            else:
                messages.info(request, 'Please Update your location')
                return redirect("profile")

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    elif request.method == 'POST' and 'signup_form':
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signup')

    else:
        form = SignUpForm()
        # return render(request, 'login2.html')
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return JsonResponse(list(cities.values('id', 'name')), safe=False)
