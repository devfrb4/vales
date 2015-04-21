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
#DJANGO REST FRAMEWORK API
from django.http import Http404
from .serializers import PersonSerializer, GoupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ================= REST FRAMEWORK API VIEWS ================================
class PersonViewList(APIView):

    def get(self,request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class PersonViewDetail(APIView):
    def get_object(self,pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_200_OK)

#  =================== /REST FRAMEWORK API VIEWS ===============================
class GroupAPiView(APIView):
    pass

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
