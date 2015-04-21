from django.contrib.auth.models import User
from .models import Person, Group
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Person
		fields = ('name', 'phone_number', 'direccion')

class GoupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('name', 'description')