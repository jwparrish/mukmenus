from django.contrib import admin
from menus.models import Menu
from menus.forms import *

class MenuAdmin(admin.ModelAdmin):
	form = DiningOptionsForm

	list_display = ('restaurant', 'genre')
	list_display_links = ('restaurant',)
	list_filter = ('restaurant', 'genre')
	list_per_page = 50
	search_fields = ['restaurant', 'genre',]

admin.site.register(Menu, MenuAdmin)
