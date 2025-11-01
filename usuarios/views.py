from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UsuarioProdutor, UsuarioAgronomo
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf', '').strip()
        senha = request.POST.get('senha', '').strip()
        cpf = ''.join(filter(str.isdigit, cpf))  # remove tudo que não for número

        if not cpf or not senha:
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'login.html')

        # Autenticação PRODUTOR
        try:
            produtor = UsuarioProdutor.objects.get(cpf=cpf)
            if produtor.verificar_senha(senha):
                request.session['usuario_tipo'] = 'produtor'
                request.session['usuario_cpf'] = produtor.cpf
                request.session['usuario_nome'] = produtor.nome
                messages.success(request, f'Bem-vindo, {produtor.nome}!')
                return redirect('/pagina_inicial_produtor/')
            else:
                messages.error(request, 'Senha incorreta.')
                return render(request, 'login.html')
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
                return render(request, 'login.html')
        except UsuarioAgronomo.DoesNotExist:
            messages.error(request, 'CPF não encontrado em nenhum cadastro.')
            return render(request, 'login.html')

    return render(request, 'login.html')

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

        # Senhas diferentes
        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'cadastro.html', {'limpar_form': True})

        # Nenhum tipo de conta selecionado
        if not tipo:
            messages.error(request, "Selecione um tipo de conta.")
            return render(request, 'cadastro.html', {'limpar_form': True})

        # PRODUTOR
        if tipo == 'Produtor':
            # Verifica duplicidade global (em ambas as tabelas)
            if (UsuarioProdutor.objects.filter(cpf=cpf).exists() or
                UsuarioAgronomo.objects.filter(cpf=cpf).exists()):
                messages.error(request, "CPF já cadastrado no sistema.")
                return render(request, 'cadastro.html', {'limpar_form': True})

            if (UsuarioProdutor.objects.filter(email=email).exists() or
                UsuarioAgronomo.objects.filter(email=email).exists()):
                messages.error(request, "E-mail já cadastrado no sistema.")
                return render(request, 'cadastro.html', {'limpar_form': True})

            # Criação
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

            user = authenticate(request, email=email, password=senha)
            if user is not None:
                login(request, user)
                messages.success(request, "Cadastro de produtor realizado com sucesso!")
                return redirect('/pagina_inicial_produtor')
            else:
                messages.warning(request, "Cadastro realizado, mas não foi possível autenticar automaticamente.")
                return redirect('/')

        # AGRÔNOMO
        elif tipo == 'Agronomo':
            # Verifica duplicidade global (CREA, CPF, e e-mail)
            if UsuarioAgronomo.objects.filter(num_crea=num_crea).exists():
                messages.error(request, "CREA já cadastrado.")
                return render(request, 'cadastro.html', {'limpar_form': True})

            if (UsuarioAgronomo.objects.filter(cpf=cpf).exists() or
                UsuarioProdutor.objects.filter(cpf=cpf).exists()):
                messages.error(request, "CPF já cadastrado no sistema.")
                return render(request, 'cadastro.html', {'limpar_form': True})

            if (UsuarioAgronomo.objects.filter(email=email).exists() or
                UsuarioProdutor.objects.filter(email=email).exists()):
                messages.error(request, "E-mail já cadastrado no sistema.")
                return render(request, 'cadastro.html', {'limpar_form': True})

            # Criação
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

            user = authenticate(request, email=email, password=senha)
            if user is not None:
                login(request, user)
                messages.success(request, "Cadastro de agrônomo realizado com sucesso!")
                return redirect('/pagina_inicial_agronomo')
            else:
                messages.warning(request, "Cadastro realizado, mas não foi possível autenticar automaticamente.")
                return redirect('/login')

        else:
            messages.error(request, "Tipo de conta inválido.")
            return render(request, 'cadastro.html', {'limpar_form': True})

    # GET
    return render(request, 'cadastro.html')

# RECUPERAÇÃO DE SENHA
def recSenha(request):
    return render(request, 'recuperarSenha.html')