from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
	# Django Admin
	path('admin/', admin.site.urls)
)