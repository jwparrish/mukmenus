from django.shortcuts import render
from menus.views import *

def frontpage(request):
	return render(request, 'frontpage.html')