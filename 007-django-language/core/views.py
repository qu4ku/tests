from django.shortcuts import render
from django.utils.translation import gettext as _
from django.http import HttpResponse

# Create your views here.
def home_view(request):
	output = _("Welcome to my site.")
	return HttpResponse(output)

def about_view(request):
	return HttpResponse('About')

def articles_view(request):
	return HttpResponse('About')