from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UsuarioProdutor, UsuarioAgronomo

def login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        #tenta achar como produto
        try:
            produtor = UsuarioProdutor.objects.get(cpf=cpf)
            if produtor.verificar_senha(senha):
                request.session['usuario_tipo'] = 'produtor'
                request.session['usuario_cpf'] = produtor.cpf
                messages.success(request, f'Bem-vindo, {produtor.nome}!')
                return redirect('inicioProdutor.html')
            else:
                messages.error(request, 'Senha incorreta.')
                return render(request, 'pgLogin.html')
        except UsuarioProdutor.DoesNotExist:
            pass  # n é produtor, tenta agronomo

        #tenta autenticar como agronomo
        try:
            agronomo = UsuarioAgronomo.objects.get(cpf=cpf)
            if agronomo.verificar_senha(senha):
                request.session['usuario_tipo'] = 'agronomo'
                request.session['usuario_crea'] = agronomo.num_crea
                messages.success(request, f'Bem-vindo, {agronomo.nome}!')
                return redirect('inicioAgronomo.html')
            else:
                messages.error(request, 'Senha incorreta.')
                return render(request, 'pgLogin.html')
        except UsuarioAgronomo.DoesNotExist:
            messages.error(request, 'CPF não encontrado em nenhum cadastro.')

    return render(request, 'pgLogin.html')


def cadastro(request):
    return render(request, 'pgCadastro.html')


def recSenha(request):
    return render(request, 'recSenha.html')
