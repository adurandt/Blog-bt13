from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):	
	return render(request, 'Home/index.html')

def Contacto(request):
	return HttpResponse('Pagina de contactos')

def Otros(request, num):
	return HttpResponse('Pagina de otros numero: <b> '+ num + '</b>')

def Saludo(reauesr, name):
	return HttpResponse('Hola, bienvenido : <b>' + name + '</b>')

def Suma(request, x, y):
	r = int(x) + int(y)
	return HttpResponse('La suma de {} + {} es de: <b>'.format(x, y) + str(r) + '</b>')

def Compara(request, x, y):
	if int(x) > int(y):
		msg = '{} es mayo que {}'.format(x, y)
	else:
		msg = '{} es mayo que {}'.format(y, x)	
	return HttpResponse(msg)	