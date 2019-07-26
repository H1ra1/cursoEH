from django.shortcuts import render
from app.models import Pessoa

# Create your views here.
def home(request):
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST['nome']
        pessoa.cpf = request.POST['cpf']
        pessoa.email = request.POST['email']
        pessoa.telefone = request.POST['telefone']
        pessoa.genero = request.POST['genero']
        try:
            pessoa.save()
            contexto = {'msg': 'Cadastro efetuado!'}
            print('Novo cadastro')
        except Exception as e:
            print(e)

    return render(request, 'index.html', contexto)

def mostar_pessoas(request):
    pessoas = Pessoa.objects.all()
    tamanho = len(pessoas)
    return render(request, 'pessoas.html', {'dados': pessoas, 'tamanho': tamanho})
