from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
	number_list = range(1, 100)
	page = request.GET.get('page', 1)
	paginator = Paginator(number_list, 20)
	try:
		numbers = paginator.page(page)
	except PageNotAnInteger:
		numbers = paginator.page(1)
	except EmptyPage:
		numbers = paginator.page(paginator.num_pages)

	return render(request, 'home.html', {'numbers': numbers})
