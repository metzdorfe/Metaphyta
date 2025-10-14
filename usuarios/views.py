from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'pgLogin.html')

def cadastro(request):
    return render(request, 'pgCadastro.html')

def recSenha(request):
    return render(request, 'recSenha.html')