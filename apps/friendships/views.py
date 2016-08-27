from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from ..loginreg.models import User
from .models import Friendships
from django.contrib import messages

# Create your views here.
def friends(request):
	context = {
		'user':User.objects.get(id=request.session['user']),
		'users':User.objects.exclude(id=request.session['user']).exclude(friendsfriend__user_id=request.session['user']).exclude(usersfriend__friend_id=request.session['user']),
		'ufriends':Friendships.objects.filter(user_id=request.session['user']),
		'ffriends':Friendships.objects.filter(friend_id=request.session['user'])
		}
	# print context['users'][0].user.alias
	return render(request, 'friendships/friends.html', context)
def show_user(request, id):
	context = {
		'users':User.objects.filter(id=id),
		}
	return render(request, 'friendships/show_user.html', context)
def delete_friend(request, id):
	friend = Friendships.objects.get(id=id)
	friend.delete()
	return redirect('/friends')
def add_friend(request):
	new_friend = Friendships.objects.create(user=User.objects.get(id=request.session['user']), friend=User.objects.get(id=request.POST['friend']))
	print new_friend
	return redirect('/friends')