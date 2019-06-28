from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def home(request):
	#f=open("index.html","r")
	#file1=loader.get_template("index1.html")	
	return HttpResponse("<h1>MyBlog Home</h1>")


def contact(request):
		return HttpResponse("<h1>Contact me</h1>")

def test1(request):
	return render(request,'myblog/test1.html')

def test2(request):
	return render(request,'myblog/test2.html')