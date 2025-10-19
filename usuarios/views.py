from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UsuarioProdutor, UsuarioAgronomo

def login(request):
    if request.method == 'POST':
        # Recebe e limpa os dados do form
        cpf = request.POST.get('cpf', '').strip()
        senha = request.POST.get('senha', '').strip()
        cpf = ''.join(filter(str.isdigit, cpf))  # remove tudo que não for número

        if not cpf or not senha:
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'pgLogin.html')

        # Autenticação PRODUTOR
        try:
            produtor = UsuarioProdutor.objects.get(cpf=cpf)
            if produtor.verificar_senha(senha):
                request.session['usuario_tipo'] = 'produtor'
                request.session['usuario_cpf'] = produtor.cpf
                request.session['usuario_nome'] = produtor.nome
                messages.success(request, f'Bem-vindo, {produtor.nome}!')
                return redirect('/pagina_inicial_produtor/')  # usa path, não arquivo .html
            else:
                messages.error(request, 'Senha incorreta.')
                return render(request, 'pgLogin.html')
        except UsuarioProdutor.DoesNotExist:
            pass  # tenta como agrônomo

        # Autenticação AGRÔNOMO
        try:
            agronomo = UsuarioAgronomo.objects.get(cpf=cpf)
            if agronomo.verificar_senha(senha):
                request.session['usuario_tipo'] = 'agronomo'
                request.session['usuario_crea'] = agronomo.num_crea
                request.session['usuario_nome'] = agronomo.nome
                messages.success(request, f'Bem-vindo, {agronomo.nome}!')
                return redirect('/pagina_inicial_agronomo/')
            else:
                messages.error(request, 'Senha incorreta.')
                return render(request, 'pgLogin.html')
        except UsuarioAgronomo.DoesNotExist:
            messages.error(request, 'CPF não encontrado em nenhum cadastro.')
            return render(request, 'pgLogin.html')

    return render(request, 'pgLogin.html')

def cadastro(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipoConta')
        nome = request.POST.get('nome', '').strip()
        sobrenome = request.POST.get('sobrenome', '').strip()
        data_nascimento = request.POST.get('dataNascimento')
        cpf = ''.join(filter(str.isdigit, request.POST.get('cpf', '')))
        telefone = request.POST.get('telefone', '').strip()
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '').strip()
        confirmar_senha = request.POST.get('confirmarSenha', '').strip()
        num_crea = request.POST.get('num_crea', '').strip()

        # Verifica se as senhas coincidem
        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'pgCadastro.html')

        # Cadastro PRODUTOR
        if tipo == 'Produtor':
            if UsuarioProdutor.objects.filter(cpf=cpf).exists():
                messages.error(request, "CPF já cadastrado.")
                return render(request, 'pgCadastro.html')

            produtor = UsuarioProdutor(
                cpf=cpf,
                nome=nome,
                sobrenome=sobrenome,
                data_nascimento=data_nascimento,
                email=email,
                telefone=telefone
            )
            produtor.set_senha(senha)
            produtor.save()
            messages.success(request, "Cadastro de produtor realizado com sucesso!")
            return redirect('/')

        # Cadastro AGRÔNOMO
        elif tipo == 'Agronomo':
            if UsuarioAgronomo.objects.filter(num_crea=num_crea).exists():
                messages.error(request, "CREA já cadastrado.")
                return render(request, 'pgCadastro.html')

            agronomo = UsuarioAgronomo(
                num_crea=num_crea,
                cpf=cpf,
                nome=nome,
                sobrenome=sobrenome,
                data_nascimento=data_nascimento,
                email=email,
                telefone=telefone
            )
            agronomo.set_senha(senha)
            agronomo.save()
            messages.success(request, "Cadastro de agrônomo realizado com sucesso!")
            return redirect('/')

        else:
            messages.error(request, "Selecione um tipo de conta.")
            return render(request, 'pgCadastro.html')

    return render(request, 'pgCadastro.html')


def recSenha(request):
    return render(request, 'recSenha.html')