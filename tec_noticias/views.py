from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import *
from .models import Contacto,Quizz


def home_page_view(request):
    return render(request, 'website/base.html')

def about_page_view(request):
    return render(request, 'website/about.html')

def apple_page_view(request):
    return render(request, 'website/apple_news.html')

def windows_page_view(request):
    return render(request, 'website/windows_news.html')

def linux_page_view(request):
    return render(request, 'website/linux_news.html')

def info_page_view(request):
    return render(request, 'website/info.html')

def contact_page_view(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tec_noticias:home'))


    context = {
        'form': form,
        'contactos':Contacto.objects.all(),
    }

    return render(request, 'website/contact.html',context)

def edita_contacto(request, email):
    contacto = Contacto.objects.get(email=email)
    form = contactForm(request.POST or None, instance=contacto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tec_noticias:home'))

    context = {'form': form, 'contacto_email': email}
    return render(request, 'website/contact_editar.html', context)

def apaga_contacto(request, email):
    Contacto.objects.get(email=email).delete()
    return HttpResponseRedirect(reverse('tec_noticias:home'))

def quizz_view(request):
    form = QuizzForm(request.POST)
    if form.is_valid():
        qz = form.save()
        return HttpResponseRedirect('resultado/'+str(qz.id))

    context = {'form': form}
    return render(request, 'website/quizz.html', context)

def quizz_resultado(request,id):
    quizz = Quizz.objects.get(id=id)
    form = QuizzForm(request.POST or None, instance=quizz)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tec_noticias:home'))

    pontos = 0

    if quizz.p1 == "nao":
        pontos+=10
    if quizz.p2 == False:
        pontos+=10
    if quizz.p3 == "Fev 25,2021":
        pontos += 10
    if quizz.p4 == "10:00 p.m.":
        pontos += 10
    if quizz.p5 == 1.57:
        pontos += 20
    if quizz.p7 == "noticias":
        pontos += 10
    if quizz.p8 == "nao":
        pontos += 10
    if quizz.p9 == "sim":
        pontos += 10
    if quizz.p10 == "Gestão de Projetos":
        pontos += 10


    context = {'quizz': quizz,'pontos':pontos}
    return render(request, 'website/quizz_resultado.html', context)
