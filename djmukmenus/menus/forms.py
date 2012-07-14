from menus.models import *
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

class DiningOptionsForm(forms.ModelForm):
	dining_options = forms.MultipleChoiceField(
		choices = DINING_OPTIONS,
		widget = CheckboxSelectMultiple,
		label = 'Dining Options',
		required = False,
	)

	class Meta:
		model = Menu
