from django.shortcuts import render
from django.utils.translation import gettext as _
from django.http import HttpResponse

from django.utils import translation
from django.conf import settings

# Create your views here.
def home_view(request):

	# print(dir(request.session))
	# output = dir(request.session)
	
	# for x in request.META:
	# 	print(x)
	
	print(request.path_info)
	# print(request.session[settings.LANGUAGE_SESSION_KEY])
	# print(request.COOKIES[settings.LANGUAGE_COOKIE_NAME])
	print(request.META['HTTP_ACCEPT_LANGUAGE'])
	print(settings.LANGUAGE_CODE)

	print(translation.get_language())
	print(request.META['LANG'])
	# print(request.headers.get('LANG'))
	from django.utils.translation import LANGUAGE_SESSION_KEY
	request.session[LANGUAGE_SESSION_KEY] = 'pl'

	translation.activate('pl')

	output = _("Welcome to my site.")
	print(output)


	return HttpResponse(output)

def about_view(request):
	return HttpResponse('About')

def articles_view(request):
	return HttpResponse('About')