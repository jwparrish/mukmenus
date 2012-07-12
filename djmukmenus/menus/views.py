from django.shortcuts import render
from menus.views import *

def home(request):
	return render(request, 'home.html')