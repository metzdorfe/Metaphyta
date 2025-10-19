from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import Perfil

# Redireciona para a página correta se já estiver logado
def home_redirect(request):
    if request.user.is_authenticated:
        perfil = Perfil.objects.get(usuario=request.user)
        if perfil.tipo_conta == 'Produtor':
            return redirect('inicioProdutor')
        else:
            return redirect('inicioAgronomo')
    return redirect('login')

# Login
def login_view(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['senha']

        try:
            perfil = Perfil.objects.get(cpf=cpf)
            user = perfil.usuario
        except Perfil.DoesNotExist:
            messages.error(request, 'CPF não cadastrado')
            return redirect('login')

        user_auth = authenticate(request, username=user.username, password=senha)
        if user_auth:
            login(request, user_auth)
            if perfil.tipo_conta == 'Produtor':
                return redirect('inicioProdutor')
            else:
                return redirect('inicioAgronomo')
        else:
            messages.error(request, 'Senha incorreta')
            return redirect('login')

    return render(request, 'pgLogin.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Páginas iniciais protegidas
@login_required(login_url='login')
def inicioProdutor(request):
    return render(request, 'pagina_inicial_produtor.html')

@login_required(login_url='login')
def inicioAgronomo(request):
    return render(request, 'pagina_inicial_agronomo.html')

# Perfis protegidos
@login_required(login_url='login')
def perfilProdutor(request):
    return render(request, 'perfil_produtor.html')

@login_required(login_url='login')
def perfilAgronomo(request):
    return render(request, 'perfil_agronomo.html')
