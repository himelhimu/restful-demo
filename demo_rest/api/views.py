from django.shortcuts import render
from rest_framework import generics
from django.contrib.staticfiles.views import serve

# Create your views here.
def get_modules(request):
    path = "/home/sabbir/Documents/curriculum.json"
    return serve(request,path=path)