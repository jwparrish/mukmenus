from django.contrib import admin
from menus.models import Menu

class MenuAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')
	list_display_links = ('title',)
	list_per_page = 50
	search_fields = ['title', 'description',]

admin.site.register(Menu, MenuAdmin)
