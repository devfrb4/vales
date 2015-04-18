from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

	def save(self, *args, **kwargs):
		self.instance.user = kwargs.pop('user', None)
		super(PersonForm, self).save(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('user', )
		# fields