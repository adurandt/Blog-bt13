from django.conf.urls import url
from views import Index, Contacto, Otros, Saludo, Suma, Compara

urlpatterns = [
	#url(r'^$', admin.site.urls),
	url(r'^index$', Index, name='index'),
	url(r'^contacto$', Contacto, name='contacto'),
	url(r'^otros/(?P<num>[0-9]+)/$', Otros, name='otros'),
	url(r'^saludo/(?P<name>[\w\s]+)/$', Saludo, name='saludo'),
	url(r'^suma/(?P<x>[0-9]+)/(?P<y>[0-9]+)/$', Suma, name='suma'),
	url(r'^compara/(?P<x>[0-9]+)/(?P<y>[0-9]+)/$', Compara, name='compara'),
	
]