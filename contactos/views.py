from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from .models import Person
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms as cForms

class PersonView(FormView):
    template_name = 'contactos/person.html'
    form_class = cForms.PersonForm

    def form_valid(self, form):
        self.success_url = reverse('contactos:get_contactos')
        form.save(user=self.request.user)
        return super(PersonView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PersonView, self).dispatch(request, *args, **kwargs)


def home(request):
    return render(request, 'index.html')


@login_required
def get_contactos(request):
    user = request.user
    contactos = Person.objects.filter(user=user)

    return render(
        request,
        'contactos/contactos.html',
        {'contactos': contactos}
    )
