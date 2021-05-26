from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
import matplotlib.pyplot as plt
# Create your views here.
from django.urls import reverse

from .forms import *
from .models import *


def home_page_view(request):
    noticias = Noticia.objects.all()

    context = {
        'lista_noticias':noticias
    }
    return render(request, 'website/base.html',context=context)

def about_page_view(request):
    return render(request, 'website/about.html')

def apple_page_view(request):
    noticias = Noticia.objects.all().filter(categoria=3)

    context = {
        'lista_noticias':noticias
    }
    return render(request, 'website/apple_news.html',context=context)

def windows_page_view(request):
    noticias = Noticia.objects.all().filter(categoria=1)

    context = {
        'lista_noticias':noticias
    }

    return render(request, 'website/windows_news.html',context=context)

def linux_page_view(request):
    noticias = Noticia.objects.all().filter(categoria=2)

    context = {
        'lista_noticias':noticias
    }
    return render(request, 'website/linux_news.html',context=context)

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

def comentario_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        comentario = form.save()
        return HttpResponseRedirect('comentario_resultados/'+str(comentario.id))


    context = {
        'form': form,
    }

    return render(request, 'website/coments.html',context)

def ver_noticia(request,id):
    noticia = Noticia.objects.get(pk=id)
    form = comentarioNoticiaForm()

    if request.method == "POST":
        autor = request.POST['autor']
        texto = request.POST['texto']
        cnt = Comentario_Noticia(None,autor,texto,date.today(),id)
        cnt.save()

    context = {
        'form':form,
        'noticia':noticia,
        'comentarios':Comentario_Noticia.objects.all().filter(ntc=id)
    }
    return render(request, 'website/ntc_detalhes.html', context)


#comentario_resultados
def comentario_resultado(request,id):
    comments = Comentario.objects.get(id=id)
    form = ComentarioForm(request.POST or None, instance=comments)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tec_noticias:home'))

    plt.bar(['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10'],[comments.campo1,str(comments.campo2),comments.campo3
                                                                  ,comments.campo4,comments.campo5,''+ str(comments.campo6)
                                                        ,comments.campo7,comments.campo8,comments.campo9,comments.campo10])
    plt.savefig('tec_noticias/static/website/imagens/plot_comentario.png',bbox_inches='tight')


    context = {'form': form}
    return render(request, 'website/coments_result.html', context)

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

    lista_pontos = []

    if quizz.p1 == "nao":
        pontos+=10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)

    if quizz.p2 == False:
        pontos+=10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)


    if quizz.p3 == "Fev 25,2021":
        pontos += 10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)


    if quizz.p4 == "10:00 p.m.":
        pontos += 10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)


    if quizz.p5 == 1.57:
        pontos += 20
        lista_pontos.append(20)
    else:
        lista_pontos.append(0)

    if quizz.p7 == "noticias":
        pontos += 10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)


    if quizz.p8 == "nao":
        pontos += 10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)

    if quizz.p9 == "sim":
        pontos += 10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)

    if quizz.p10 == "Gestão de Projetos":
        pontos += 10
        lista_pontos.append(10)
    else:
        lista_pontos.append(0)


    plt.bar(['p1','p2','p3','p4','p5','p7','p8','p9','p10'],lista_pontos)
    plt.savefig('tec_noticias/static/website/imagens/plot.png',bbox_inches='tight')


    context = {'quizz': quizz,'pontos':pontos}
    return render(request, 'website/quizz_resultado.html', context)

#login
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
    return render(request, 'website/login.html', {
        'message': 'Logged out'})