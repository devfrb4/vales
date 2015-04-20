from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView

class Login(FormView):
	template_name = 'accounts/login.html'
	form_class = AuthenticationForm
	success_url = '/'

	def form_valid(self, form):
		self.success_url = reverse('contactos:get_contactos')
		auth_login(self.request, form.get_user())
		return super(Login, self).form_valid(form)

	def dispatch(self, request, *args, **kwargs):
		#Validate that user is not already logged in.
		if request.user.is_authenticated():
			return redirect(self.success_url)
		return super(Login, self).dispatch(request, *args, **kwargs)

class Register(View):
	form_class = UserCreationForm
	template_name = 'accounts/register.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:login'))
		else:
			return render(request, self.template_name, {'form': form}) 
