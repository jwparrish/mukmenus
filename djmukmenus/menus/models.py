from django.db import models
from settings import *

class Menu(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	file = models.FileField(upload_to=MEDIA_ROOT, blank=True)