from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import UsuarioAgronomo, UsuarioProdutor
from main_pages.models import FotoPerfil
from analises.models import Propriedade

def pagina_inicial_agronomo(request):
    if request.session.get('usuario_tipo') != 'agronomo':
        messages.error(request, "Acesso restrito a contas de agrônomo.")
        return redirect('/')

    crea = request.session.get('usuario_crea')
    try:
        agronomo = UsuarioAgronomo.objects.get(num_crea=crea)
    except UsuarioAgronomo.DoesNotExist:
        messages.error(request, "Agrônomo não encontrado.")
        return redirect('/')

    notificacoes = [
        #tem q adicionar ainda
    ]

    clientes = agronomo.produtores.all()

    clientes_info = []
    for cli in clientes:
        foto = FotoPerfil.objects.filter(produtor=cli).first()
        propriedades = Propriedade.objects.filter(produtor=cli)

        clientes_info.append({
            "cliente": cli,
            "foto": foto,
            "propriedades": propriedades,
        })

    context = {
        "nome": agronomo.nome,
        "sobrenome": agronomo.sobrenome,
        "clientes": clientes_info,
        "notificacoes": notificacoes,
    }

    return render(request, "indexAgronomo.html", context)



def pagina_inicial_produtor(request):
    if request.session.get('usuario_tipo') != 'produtor':
        messages.error(request, "Acesso restrito a contas de produtor.")
        return redirect('/')

    cpf = request.session.get('usuario_cpf')
    try:
        produtor = UsuarioProdutor.objects.get(cpf=cpf)
    except UsuarioProdutor.DoesNotExist:
        messages.error(request, "Produtor não encontrado.")
        return redirect('/')

    notificacoes = [
        #tem q adicionar ainda
    ]

    propriedades = produtor.propriedades.all()

    context = {
        "nome": produtor.nome,
        "sobrenome": produtor.sobrenome,
        "propriedades": propriedades,
        "notificacoes": notificacoes,
    }

    return render(request, "indexProdutor.html", context)



def perfilAgronomo(request):
    if request.session.get('usuario_tipo') != 'agronomo':
        messages.error(request, "Acesso restrito a contas de agrônomo.")
        return redirect('/')

    crea = request.session.get('usuario_crea')

    try:
        usuario = UsuarioAgronomo.objects.get(num_crea=crea)
    except UsuarioAgronomo.DoesNotExist:
        messages.error(request, "Agrônomo não encontrado.")
        return redirect('/')

    foto = FotoPerfil.objects.filter(agronomo=usuario).first()

    context = {
        "usuario": usuario,
        "foto": foto
    }

    return render(request, "perfilAgronomo.html", context)



def perfilProdutor(request):
    if request.session.get('usuario_tipo') != 'produtor':
        messages.error(request, "Acesso restrito a contas de produtor.")
        return redirect('/')

    cpf = request.session.get('usuario_cpf')

    try:
        produtor = UsuarioProdutor.objects.get(cpf=cpf)
    except UsuarioProdutor.DoesNotExist:
        messages.error(request, "Produtor não encontrado.")
        return redirect('/')

    foto = FotoPerfil.objects.filter(produtor=produtor).first()

    context = {
        "produtor": produtor,
        "foto": foto,
    }

    return render(request, "perfilProdutor.html", context)