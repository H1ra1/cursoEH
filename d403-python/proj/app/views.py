from django.shortcuts import render
from app.models import Pessoa

# Create your views here.
def home(request):
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST['nome']
        pessoa.cpf = request.POST['cpf']
        pessoa.save()

    return render(request, 'index.html')

def mostar_pessoas(request):
    pessoas = Pessoa.objects.all()
    tamanho = len(pessoas)
    return render(request, 'pessoas.html', {'dados': pessoas, 'tamanho': tamanho})
