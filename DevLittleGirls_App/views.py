from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, __all__
from DevLittleGirls_App.models import Site, Aluno

def site_list(request):
    site = Site.objects.all()
    aluno = Aluno.objects.all()
    context = {
        'tb_site_list': site,
        'tb_aluno_list': aluno,
    }
    return render(request, 'site_list.html', context)