from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..loginreg.models import User
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'main/index.html')