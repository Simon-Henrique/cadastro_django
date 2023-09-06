from django.shortcuts import render
from .models import user

def home(request):
    return render(request, 'users/home.html')

def listagem(request):
    #salvando dados no db
    new_user = user() #instanciando a classe
    new_user.idade = request.POST.get('insert_idade') #pegando os dados do input no front e jogando no model
    new_user.nome = request.POST.get('insert_nome') #pegando os dados do input no front e jogando no model
    new_user.save() 
    #exibindo usuarios cadastrados: 
    users = {
        'users': user.objects.all()
    }
    #retornar dados para a pagina de usuarios
    return render(request, 'users/listagem_users.html', users) #irá renderizar na rota destino, o dict users, que pegou todos os dados do db

def lista(request):
    lista_users = {
        'users': user.objects.all()
    }
    return render(request, 'users/listagem2.html', lista_users)