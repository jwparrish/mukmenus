from django.contrib import admin

from djmukmenus.menus.models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display  = ('restaurant', 'modified', 'menu_pdf', 'menu_png')
    readonly_fields = ('modified',)
    search_fields = ('name',)

admin.site.register(Menu, MenuAdmin)
