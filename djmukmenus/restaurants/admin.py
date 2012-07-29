from django.contrib import admin

from djmukmenus.restaurants.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display  = ('admin_thumbnail', 'name', 'phone', 'website', 
                     'modified', 'active')
    search_fields = ('name',)
    readonly_fields = ('modified',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Restaurant, RestaurantAdmin)
