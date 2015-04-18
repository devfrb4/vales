from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from .models import Person
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms as cForms


class PersonView(View):
    template_name = 'contactos/person.html'

    def get(self, request):
        form = cForms.PersonForm()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = cForms.PersonForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect(reverse('contactos:get_contactos'))
        else:
            return render(request, self.template_name, locals())

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
