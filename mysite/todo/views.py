from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def todo(request):
  return HttpResponse("Hello, my Name is Marty!")

	
