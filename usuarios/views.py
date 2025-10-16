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
    if request.method == 'POST':
        tipo = request.POST.get('tipoConta')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        data_nascimento = request.POST.get('dataNascimento')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmarSenha')
        num_crea = request.POST.get('num_crea')  # só usado para agrônomo

        # Verifica se as senhas batem
        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'pgCadastro.html')

        # Cria PRODUTOR
        if tipo == 'Produtor':
            if UsuarioProdutor.objects.filter(cpf=cpf).exists():
                messages.error(request, "CPF já cadastrado.")
                return render(request, 'pgCadastro.html')
            usuario = UsuarioProdutor(
                cpf=cpf,
                nome=nome,
                sobrenome=sobrenome,
                data_nascimento=data_nascimento,
                email=email,
                telefone=telefone
            )
            usuario.set_senha(senha)
            usuario.save()
            messages.success(request, "Cadastro de produtor realizado com sucesso!")
            return redirect('pgLogin.html')

        # Cria AGRÔNOMO
        elif tipo == 'Agronomo':
            if UsuarioAgronomo.objects.filter(num_crea=num_crea).exists():
                messages.error(request, "CREA já cadastrado.")
                return render(request, 'pgCadastro.html')
            usuario = UsuarioAgronomo(
                num_crea=num_crea,
                cpf=cpf,
                nome=nome,
                sobrenome=sobrenome,
                data_nascimento=data_nascimento,
                email=email,
                telefone=telefone
            )
            usuario.set_senha(senha)
            usuario.save()
            messages.success(request, "Cadastro de agrônomo realizado com sucesso!")
            return redirect('pgLogin.html')

        else:
            messages.error(request, "Selecione um tipo de conta.")
            return render(request, 'pgCadastro.html')

    # GET
    return render(request, 'pgCadastro.html')


def recSenha(request):
    return render(request, 'recSenha.html')
