from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index(request):
    filmes = ['O Poderoso Chefão', 'Um Sonho de Liberdade', 'O Senhor dos Anéis']
    context = {'filmes': filmes}
    return render(request, 'index.html', context)

