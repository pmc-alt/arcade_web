from django.shortcuts import render

def home(request):
	return render(request, 'home.html',{})

def request(request):
	return render(request, 'request.html',{})