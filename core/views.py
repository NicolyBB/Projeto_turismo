from django.shortcuts import render

# A função render() busca e processa o seu arquivo de template
def home(request):
    return render(request, 'index.html')

def historia(request):
    return render(request, 'historia.html')

def atracoes(request):
    return render(request, 'atracoes.html')

def galeria(request):
    return render(request, 'galeria.html')
