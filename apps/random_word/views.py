from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
def index(request):
	context = {
		'word':get_random_string(length=14)
	}
	return render( request, 'index.html', context)
def new(request):
	return redirect('/')