from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = {}
    data [ 'nome' ] = 'Kleber Vascocelos'
    return render(request, 'index.html')


def form(request):
    return render(request, 'form.html')