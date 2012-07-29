# -*- coding: utf-8 -*-

import datetime as dt

from django.db import models
from django.forms import ModelForm

from djmukmenus.restaurants.managers import RestaurantManager


class Restaurant(models.Model):
    """Menus belong to restaurants."""
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, max_length=140)
    
    active = models.BooleanField(default=True)
    
    logo = models.ImageField(blank=True, upload_to='restaurant_logos')
    
    addr_line1 = models.CharField("Line 1", blank=True, max_length=100)
    addr_line2 = models.CharField("Line 2", blank=True, max_length=100)
    addr_city  = models.CharField("City", blank=True, max_length=75)
    addr_zip = models.CharField("Zip", blank=True, max_length=20)
    
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    
    # Make note that we're overiding the default manager here.
    objects = RestaurantManager()
    
    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = dt.datetime.today()
        self.modified = dt.datetime.now()
        super(Ticket, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('name', 'modified')
    
    def __unicode__(self):
        return "%s" % self.restaurant
    
    @models.permalink
    def get_absolute_url(self):
        return ('restaurant_detail', (), {'slug': self.slug})
