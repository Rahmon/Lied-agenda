from django.shortcuts import render
import requests
import json

# Create your views here.

def lista(request):
    url = 'http://127.0.0.1:8000/contato'
    r = requests.get(url)
    data = json.loads(r.text)
    
    return render(request, 'lista.html', {'contatos': data['results']})

def ver_contato(request, pk):
    url = 'http://127.0.0.1:8000/contato/' + pk
    r = requests.get(url)
    data = json.loads(r.text)
    
    return render(request, 'contato.html', {'contato': data})
    
