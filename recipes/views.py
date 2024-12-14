from django.shortcuts import render
from django.http import HttpResponse

def home_receitas(request):
    return render(request, 'home/home.html', context = {'name': 'PEsro v0-fkdslof,mdsfdsoiçfcmzd op vfkldsak'})
    #return render(request, 'home.html')