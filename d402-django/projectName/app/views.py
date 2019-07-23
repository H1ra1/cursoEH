from django.shortcuts import render

def home(request):
    lista_de_comidas = ['banana', 'torta', 'lasanha', 'macarrão']
    parametros = {
        'comidas': lista_de_comidas
    }
    return render(request, 'index.html', parametros)

def pagina2(request):
    return render(request, 'pagina2.html')