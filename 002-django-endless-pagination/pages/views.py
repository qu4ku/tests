from django.shortcuts import render

# Create your views here.
def home(request):
	numbers = list(range(1000))
	context = {'numbers': numbers}
	return render(request, 'home.html', context)