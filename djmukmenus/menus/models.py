from django.db import models
from settings import *

# Needed to save as integer because string was not showing selections when viewing menu object in Admin
DINING_OPTIONS = (
		(1,'Dine In'),
		(2, 'Carry Out'),
	)

GENRES = (
		('chinese', 'Chinese'),
		('american','American'),
		('mexican', 'Mexican'),
		('greek', 'Greek'),
		('indian', 'Indian'),
		('german', 'German'),
		('italian', 'Italian'),
		('fastfood', 'Fast Food'),
		('thai', 'Thai'),
	)

class Menu(models.Model):
	restaurant = models.CharField(max_length=200)
	genre = models.CharField(max_length=60, choices=GENRES)
	phonenumber = models.CharField(max_length=20, verbose_name='phone number')
	website = models.CharField(max_length=200)
	dining_options = models.CharField(max_length=200)
	menu = models.FileField(upload_to=MEDIA_ROOT, blank=True)
	menu_thumb = models.FileField(upload_to=MEDIA_ROOT, blank=True, verbose_name='menu thumbnail')