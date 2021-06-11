import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
# Create your views here.
from django.urls import reverse

from .forms import *
from .models import *
from .data import retornaDados

def index(request):
    return render(request, "website/home.html",context={'quizz_visible': 'none','comment_visible':'none'})

def section(request, num):
    if num == "comentario":
        form = ComentarioForm()
        context = {
            'form':form
        }
        return render(request,'website/coments.html',context)
    if num == "quizz":
        form = QuizzForm()
        context = {
            'form':form
        }
        return render(request,'website/quizz.html',context)
    if num == "about":
        return render(request,'website/about.html')
    if num == "contactos":
        form = contactForm()
        context = {
            'form': form,
            'contactos': Contacto.objects.all(),
        }
        return render(request,'website/contact.html',context)
    if num == "login":
        return render(request,'website/login.html')
    if num == "home":
        codigo = "<h1> 😄 💻 📱 Vem Vindo a TecNewsTuga ⚽ 🔥</h1>" \
        +        "<p> Esperamos que gostem do nosso website " \
        +         "Feito em Django e em JavaScript usando DOM e outras magias da web....</p> " \
                  "<p>Espero que gostem do website e da sua estrutura." \
                  "Se visualizar erros ou falhas, contacte no formulario comentarios..." \
                  "Esteja sempre informado com a nossa Agencia Noticiaria de Tecnologia !!! </p>"
        return HttpResponse(codigo)
    if num == "apple":
        return HttpResponse("")
    if num == "linux":
        return HttpResponse("")
    if num == "windows":
        return HttpResponse("")
    if num == "showQuizzResults":
        return render(request, "website/home.html", context={'quizz_visible': 'block','pontos':pontos,'comment_visible':'none'})
    if num == "showCommentsResults":
        return render(request, "website/home.html",context={'quizz_visible': 'none','comment_visible': 'block'})
    else:
        raise Http404("No such section")

def guarda_contacto(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tec_noticias:home'))

    context = {
        'form': form,
        'contactos': Contacto.objects.all(),
    }

    return render(request, 'website/contact.html', context)

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


def comentario_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save()

        comments = Comentario.objects.get(id=comentario.id)
        plt.bar(['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10'],
                [comments.campo1, str(comments.campo2), comments.campo3
                    , comments.campo4, comments.campo5, '' + str(comments.campo6)
                    , comments.campo7, comments.campo8, comments.campo9, comments.campo10])
        plt.savefig('tec_noticias/static/website/imagens/plot_comentario.png', bbox_inches='tight')

        return section(request,'showCommentsResults')

def quizz_view(request):
    form = QuizzForm(request.POST)
    if form.is_valid():
        quizz_form = form.save()

        quizz = Quizz.objects.get(id=quizz_form.id)
        global pontos
        pontos = 0

        respostas_recebidas = [quizz.p1, str(quizz.p2), str(quizz.p3), str(quizz.p4), str(quizz.p5),
                               quizz.p7, quizz.p8, quizz.p9, quizz.p10]

        respostas_certas = ['nao', False, 'Fev 25,2021', '10:00 p.m.', '1.57', 'noticias', 'nao', 'sim',
                            'gestao de projetos']
        lista_pontos = []

        pontos += 20
        for i in range(0, len(respostas_recebidas)):
            if respostas_recebidas[i] == respostas_certas[i]:
                lista_pontos.append(10)
                pontos += 10
            else:
                lista_pontos.append(0)


        plt.bar(['p1', 'p2', 'p3', 'p4', 'p5', 'p7', 'p8', 'p9', 'p10'], lista_pontos)
        plt.savefig('tec_noticias/static/website/imagens/plot.png', bbox_inches='tight')

        return section(request,'showQuizzResults')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
                    request,
                    username=username,
                    password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tec_noticias:home'))
        else:
            return render(request, 'website/login.html', {
                'message': 'Credenciais inválidas! Tente Novamente.'
            })

    return render(request, 'website/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'website/home.html', {
        'message': 'Logged out'})

def Get_Noticias(request):
    return HttpResponse(retornaDados())