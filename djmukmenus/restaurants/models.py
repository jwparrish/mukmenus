# -*- coding: utf-8 -*-

import datetime as dt

from django.db import models

from tagging.fields import TagField
import tagging

from djmukmenus.restaurants.managers import RestaurantManager


class Restaurant(models.Model):
    """Menus belong to restaurants."""
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, max_length=140)
    
    active = models.BooleanField(default=True)
    
    logo = models.ImageField(blank=True, upload_to='restaurant_logos')
    website = models.URLField(blank=True, verify_exists=False)
    phone = models.CharField(blank=True, max_length=20)
    
    tags = TagField(help_text="Comma separated")
    
    addr_line1 = models.CharField("Line 1", blank=True, max_length=100)
    addr_line2 = models.CharField("Line 2", blank=True, max_length=100)
    addr_city  = models.CharField("City", blank=True, max_length=75)
    addr_zip = models.CharField("Zip", blank=True, max_length=20)
    
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    
    # Make note that we're overiding the default manager here.
    objects = RestaurantManager()
    
    def admin_thumbnail(self):
        if self.logo:
            return u'<img src="%s" style="width:40px; height:40px;"/>' % \
            self.logo.url
        else:
            return u'N/A'
    admin_thumbnail.short_description = "Logo"
    admin_thumbnail.allow_tags = True
    
    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = dt.datetime.today()
        self.modified = dt.datetime.now()
        super(Restaurant, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('name', 'modified')
    
    def __unicode__(self):
        return "%s" % self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('restaurant_detail', (), {'slug': self.slug})
