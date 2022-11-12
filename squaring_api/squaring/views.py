from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.

class squaringView(View):
    def get(self, request, number):
        return HttpResponse(number ** 2)

class HelloworldView(View):
    def get(self, request, name):
        return HttpResponse(f'Hello world, {name}!')

