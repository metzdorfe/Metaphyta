from django.shortcuts import render, redirect

def addPropriedade(request):
    return render(request, 'addPropriedade.html')

def propriedade(request):
    return render(request, 'propriedade.html',)


def addTalhao(request):
    return render(request, 'addTalhao.html')


def addAnalise(request):
    return render(request, 'addAnalise.html')