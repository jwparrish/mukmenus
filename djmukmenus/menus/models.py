# -*- coding: utf-8 -*-

import datetime as dt

from django.db import models
from django.forms import ModelForm

from djmukmenus.restaurants.models import Restaurant
from djmukmenus.menus.managers import MenuManager


class Menu(models.Model):
    """A restaurant menu and meta surrounding it."""
    
    restaurant = models.ForeignKey(Restaurant)
    
    menu_pdf = models.FileField(blank=True, upload_to='restaurant_menus')
    menu_png = models.ImageField(blank=True, upload_to='restaurant_menus')
    
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    
    # Make note that we're overiding the default manager here.
    objects = MenuManager()
    
    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = dt.datetime.today()
        self.modified = dt.datetime.now()
        super(Menu, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('restaurant__name', 'modified')
    
    def __unicode__(self):
        return "%s's Menu" % self.restaurant
    
    @models.permalink
    def get_absolute_url(self):
        # In the future, I'd like to see the unique identifier for menus to me
        # in timestamp format. E.g.: ``mukmenus.com/fork-in-the-road/20120420``
        return ('menu_detail', (), {'pk': self.pk})
