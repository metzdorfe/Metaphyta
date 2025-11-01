from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import UsuarioAgronomo, UsuarioProdutor  # importa do teu app de login

def pagina_inicial_agronomo(request):
    # Verifica se o usuário logado é agrônomo
    if request.session.get('usuario_tipo') != 'agronomo':
        messages.error(request, "Acesso restrito a contas de agrônomo.")
        return redirect('/')

    crea = request.session.get('usuario_crea')
    try:
        agronomo = UsuarioAgronomo.objects.get(num_crea=crea)
    except UsuarioAgronomo.DoesNotExist:
        messages.error(request, "Agrônomo não encontrado.")
        return redirect('/')

    # clientes = UsuarioProdutor.objects.filter(agronomo_relacionado=agronomo)
    # Por enquanto, exemplo fixo:
    clientes = [
        #{"nome": "Carlos Almeida", "propriedade": "Fazenda Boa Esperança"},
        #{"nome": "Fernanda Souza", "propriedade": "Sítio Primavera"},
    ]

    # Simulação de notificações (depois pode vir do banco)
    notificacoes = [
        #{"texto": "Cliente Carlos enviou uma nova solicitação de análise.", "tempo": "Há 2 horas"},
        #{"texto": "Relatório de campo atualizado com sucesso.", "tempo": "Ontem, 14:22"},
    ]

    context = {
        "nome": agronomo.nome,
        "sobrenome": agronomo.sobrenome,
        "clientes": clientes,
        "notificacoes": notificacoes,
    }

    return render(request, "indexAgronomo.html", context)

def pagina_inicial_produtor(request):
    # Verifica se o usuário logado é produtor
    if request.session.get('usuario_tipo') != 'produtor':
        messages.error(request, "Acesso restrito a contas de produtor.")
        return redirect('/')

    cpf = request.session.get('usuario_cpf')
    try:
        produtor = UsuarioProdutor.objects.get(cpf=cpf)
    except UsuarioProdutor.DoesNotExist:
        messages.error(request, "Produtor não encontrado.")
        return redirect('/')

    # Exemplo fixo de propriedades
    propriedades = [
        #{"nome": "Fazenda Boa Esperança", "local": "São Paulo"},
        #{"nome": "Sítio Primavera", "local": "Minas Gerais"},
    ]

    # Exemplo fixo de notificações
    notificacoes = [
        #{"texto": "Nova análise disponível para sua propriedade.", "tempo": "Hoje, 10:30"},
        #{"texto": "Atualização do clima enviada.", "tempo": "Ontem, 18:15"},
    ]

    context = {
        "nome": produtor.nome,
        "sobrenome": produtor.sobrenome,
        "propriedades": propriedades,
        "notificacoes": notificacoes,
    }

    return render(request, "indexProdutor.html", context)