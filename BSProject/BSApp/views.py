from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post
#from .forms import loginForm,RegisterForm

def index(req):
	posts=Post.objects.all().order_by('-time') # getting all the fields from model
	return render(req,'index.html',{'posts':posts})

def final(request):
	return render(request,'final.html')


def post_details(req,slug):
	post=Post.objects.get(slug=slug) # getting only slug field
	return render(req,'post_details.html',{'post':post}) # getting the objects in post here

