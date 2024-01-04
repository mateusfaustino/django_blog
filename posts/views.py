from django.shortcuts import render
from django.http import HttpResponse

def posts(request):
    return HttpResponse("posts")

def post(request):
    return HttpResponse("post")