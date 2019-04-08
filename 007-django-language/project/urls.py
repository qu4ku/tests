from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
# from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _

from core import views


urlpatterns = [
    # path('', include('core.urls')),
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
	# Django Admin
	path('', views.home_view, name='home'),
	path('admin/', admin.site.urls),
	path(_('about/'), views.about_view, name='about'),
	path(_('articles/'), views.articles_view, name='articles'),
	prefix_default_language=False,
)

# print(_('articles/'))
# print(path(_('articles/'), views.articles_view, name='articles'))


# from django.utils.translation import activate
# from django.urls import reverse


# for lang in ['en', 'pl']:
# 	activate(lang)
# 	print(_('articles/'))
# 	print(reverse('articles'))
# 	print(_('articles/'))

