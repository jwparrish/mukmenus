from django.shortcuts import render
from menus.models import Menu

def frontpage(request):
	menus = Menu.objects.all().order_by('-id')
	return render(request, 'frontpage.html', { 'menus': menus })