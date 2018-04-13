from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User



# =================================================
# 						HELPERS
# =================================================
def current_user(request):

    return User.objects.get(id=request.session['user_id'])


def flash_errors(request, errors):

    for error in errors:

        messages.error(request, error)

# ==============================================================
# 						RENDER
# ==============================================================
def index(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = current_user(request)
    context = {
        'user': user, 
        'nonfriends': User.objects.exclude(friends=User.objects.get(id=request.session["user_id"])).exclude(id=request.session["user_id"])
    }
    return render(request, 'friends/index.html', context)

def show_user(request, userid):
    user = User.objects.get(id = userid)
    context = {
        'user': user,
        }
    return render(request, 'friends/users.html', context)

# ==============================================================
#                       PROCESS
# ==============================================================


def add_friend(request, friendid):
    User.objects.add_friend(friendid, request.session["user_id"])
    return redirect('dashboard')

def remove_friend(request, friendid):
    User.objects.remove_friend(friendid, request.session["user_id"])
    return redirect('dashboard')