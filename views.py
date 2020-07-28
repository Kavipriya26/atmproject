from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framewok import viewsets
from models import register,authentication,deposit,withdraw
from rest_framework.response import Response

class registerviewset(viewsets.Modelviewset):
	queryset=register.object.all().order_by('_id')
	Serializer_class=registerSerializer
def create(self,request, *args, **kwargs):
	try:
		Serializer=registerSerializer(data=requestdata)
		Serializer.is_valid(raise_exception=True)
		Serializer.save()
		return Response(Serializer.data)
except Exception as e:
	 print('e--',e)
def destroy(self,request,*args,**kwargs)
	instance=self.get_object()
	instance.delete()
	
class authenticationviewset(viewsets.Modelviewset):
	queryset=register.object.all().order_by('_id')
	Serializer_class=registerSerializer
def create(self,request, *args, **kwargs):
	try:
		Serializer=registerSerializer(data=requestdata)
		Serializer.is_valid(raise_exception=True)
		Serializer.save()
		return Response(Serializer.data)
except Exception as e:
	 print('e--',e)
def destroy(self,request,*args,**kwargs)
	instance=self.get_object()
	instance.delete()

class depositviewset(viewsets.Modelviewset):
	queryset=register.object.all().order_by('_id')
	Serializer_class=registerSerializer
def create(self,request, *args, **kwargs):
	try:
		Serializer=registerSerializer(data=requestdata)
		Serializer.is_valid(raise_exception=True)
		Serializer.save()
		return Response(Serializer.data)
except Exception as e:
	 print('e--',e)
def destroy(self,request,*args,**kwargs)
	instance=self.get_object()
	instance.delete()

class withdrawviewset(viewsets.Modelviewset):
	queryset=register.object.all().order_by('_id')
	Serializer_class=registerSerializer
def create(self,request, *args, **kwargs):
	try:
		Serializer=registerSerializer(data=requestdata)
		Serializer.is_valid(raise_exception=True)
		Serializer.save()
		return Response(Serializer.data)
except Exception as e:
	 print('e--',e)
def destroy(self,request,*args,**kwargs)
	instance=self.get_object()
	instance.delete()
	

	

	
