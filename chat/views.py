
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import chatMessages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserModel
from django.db.models import Q
import json
from accounts.models import Profile, City
from .filters import UserFilter
# Create your views here.


def search(request):
    User = get_user_model()
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})


@login_required(login_url='/account/')
def home(request):
    if request.user.profile.city is not None and request.user.last_name is not '':
        User = get_user_model()
        city_list = City.objects.all()
        chats = {}
        city = request.GET.get("city")
        selected_city = request.user.profile.filter_city_id
        if city is not None:
            users = User.objects.filter(profile__city=city)
            Profile.objects.filter(filter_city_id=request.user.profile.filter_city_id).update(
                filter_city_id=city)
        else:
            users = User.objects.filter(profile__city=selected_city)

        user_filter = UserFilter(request.GET, queryset=users)
        print(city)
        if request.method == 'GET' and 'u' in request.GET:
            # chats = chatMessages.objects.filter(Q(user_from=request.user.id & user_to=request.GET['u']) | Q(user_from=request.GET['u'] & user_to=request.user.id))
            chats = chatMessages.objects.filter(Q(user_from=request.user.id, user_to=request.GET['u']) | Q(
                user_from=request.GET['u'], user_to=request.user.id))
            chats = chats.order_by('date_created')
        context = {
            "selected_city": selected_city,
            "cities": city_list,
            'filter': user_filter,
            "page": "home",
            "users": users,
            "chats": chats,
            "chat_id": int(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0)
        }
        print(request.GET['u'] if request.method ==
              'GET' and 'u' in request.GET else 0)
        return render(request, "chat_home.html", context)
    else:
        messages.info(
            request, 'Please Update your location or Name')
        return redirect("profile")


def get_messages(request):
    chats = chatMessages.objects.filter(Q(id__gt=request.POST['last_id']), Q(
        user_from=request.user.id, user_to=request.POST['chat_id']) | Q(user_from=request.POST['chat_id'], user_to=request.user.id))
    new_msgs = []
    for chat in list(chats):
        data = {}
        data['id'] = chat.id
        data['user_from'] = chat.user_from.id
        data['user_to'] = chat.user_to.id
        data['message'] = chat.message
        data['date_created'] = chat.date_created.strftime("%b-%d-%Y %H:%M")
        print(data)
        new_msgs.append(data)
    return HttpResponse(json.dumps(new_msgs), content_type="application/json")


def send_chat(request):
    resp = {}
    User = get_user_model()
    if request.method == 'POST':
        post = request.POST

        u_from = UserModel.objects.get(id=post['user_from'])
        u_to = UserModel.objects.get(id=post['user_to'])
        insert = chatMessages(
            user_from=u_from, user_to=u_to, message=post['message'])
        try:
            insert.save()
            resp['status'] = 'success'
        except Exception as ex:
            resp['status'] = 'failed'
            resp['mesg'] = ex
    else:
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")
