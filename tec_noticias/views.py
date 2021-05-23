from django.http import HttpResponseRedirect
from django.shortcuts import render
import matplotlib.pyplot as plt
# Create your views here.
from django.urls import reverse

from .forms import *
from .models import *


def home_page_view(request):
    news = {
        'nome':'Bodhi Linux 6.0.0: Distro baseada no Ubuntu com interface levezinha',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2021/05/bodhi_00.jpg',
        'Autor':'Linux 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'O Bodhi Linux é uma pequena, mas potente distribuição, que pode ser personalizada de '
                    'acordo com as necessidades de cada utilizador. Esta distribuição é uma semi-rolling distro,'
                    ' baseada no Ubuntu e vem com um conjunto de ferramentas pré-instaladas, como o Midori, LXTerminal, '
                    'PCManFM, Leafpad ou o Synaptic.'
    }

    news2 = {
        'nome':'Dica: Como ter já a atualização de maio de 2021 no Windows 10',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2021/04/windows_10_1.jpg',
        'Autor':'Windows 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'O dia de ontem foi rico em novidades em várias frentes. '
                    'Se a mais visível foi a chegada do Android 12, a verdade é que a Microsoft preparou uma surpresa'
                    'para os utilizadores do Windows 10, com uma novidade já esperada.'
    }

    news3 = {
        'nome': 'App Atalhos: Gerar QR Code para partilhar rede Wi-Fi',
        'img': 'https://pplware.sapo.pt/wp-content/uploads/2021/05/appatalhos-1.jpeg',
        'Autor': 'Apple 23 Maio 2021',
        'tipo': 'phone',
        'Descrição': 'Depois de lhe termos mostrado um pouco do que é a App Atalhos e o que é possível fazer e criar com '
                     'esta enorme aplicação, decidimos não ficar por ali. '
                     'Quantas vezes já recebeu pessoas em casa e deu por si numa desorganização total por causa do acesso ao '
                     'Wi-Fi? Existe uma forma muito simples de partilhar a sua rede.'
    }


    noticias = {
        'titulos': [news,news2,news3]
    }
    return render(request, 'website/base.html',context=noticias)

def about_page_view(request):
    return render(request, 'website/about.html')

def apple_page_view(request):
    news = {
        'nome':'5 aplicações importantes para ter no seu macOS Big Sur',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2020/11/assistente_migracao_macOS_big_sur_0.jpg',
        'Autor':'Apple 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'É de conhecimento comum que os sistemas operativos trazem já muitas e boas ferramentas nativas. '
                    'Como tal, também o macOS Big Sur vem equipado com muitas aplicações e serviços.'
                    'No entanto, podemos sempre instalar gratuitamente aplicações que sejam mais à nossa imagem.'
                    'O que trazemos hoje, para quem tem macOS, são 5 ferramentas gratuitas e muito úteis.'
    }

    news2 = {
        'nome':'Afinal já é possível correr o Windows nos Mac com SoC M1 da Apple',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2020/11/macbook_m1_apple.jpg',
        'Autor':'Apple 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'Criados e desenhados para correr o macOS, os novos SoC M1 da Apple têm um desempenho que os coloca '
                    'quase como um novo padrão no mercado. Por essa razão os utilizadores querem experimentá-los noutros '
                    'contextos e certamente noutras plataformas.'
    }

    news3 = {
        'nome': 'Será o iPhone 13 o primeiro iPhone que não terá nenhuma porta?',
        'img': 'https://pplware.sapo.pt/wp-content/uploads/2020/11/iphone_13_sem_porta01.jpg',
        'Autor': 'Apple 23 Maio 2021',
        'tipo': 'phone',
        'Descrição': 'A Apple sempre pautou a sua oferta com várias tecnologias desenhadas por si em pontos determinantes.'
                     'As portas de comunicação e alimentação são um desses exemplos. Apesar de atualmente haver já uma porta'
                     'que compete com a Lightning, esta foi a mais avançada, '
                     'dentro do segmento, durante anos. Agora, com a chegada do iPhone 12 e um carregamento sem fios '
                     'melhorado, será que vão haver mudanças radicais?'
    }


    noticias = {
        'titulos': [news,news2,news3]
    }
    return render(request, 'website/apple_news.html',context=noticias)

def windows_page_view(request):
    news = {
        'nome':'Atualização do Windows 10 traz problemas no acesso ao Microsoft Teams e Outlook',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2020/11/pplware_windows_10_alerta_atualizacao_1.jpg',
        'Autor':'Windows 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'Com uma grande atualização a ser passada aos utilizadores do Windows 10,'
                    'é normal que este sistema esteja com uma atenção particular. Os utilizadores'
                    'procuram avaliar se existem problemas ou situações anormais.'
    }

    news2 = {
        'nome':'Dica: Que placa gráfica tem no seu Windows 10? Destas 3 formas sabe de imediato',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2021/05/windows_10x_1.jpg',
        'Autor':'Windows 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'Qualquer utilizador quer saber o hardware e os diferentes elementos que tem no seu computador. '
                    'Desta forma conseguem manter a sua máquina monitorizada e preparada para todas as situações '
                    'que lhe forem apresentadas.No campo da placa gráfica, existem várias formas de '
                    'saber o que está presente. Desde ferramentas próprias do Windows 10 até a propostas externas, '
                    'tudo pode deve ser usado para dar esta informação'
    }

    news3 = {
        'nome': 'Dica: Mostrar todos os dados do CPU no Gestor de Tarefas de Windows 10',
        'img': 'https://pplware.sapo.pt/wp-content/uploads/2020/06/pplware_windows_10_reinstalar_cloud_0.jpg',
        'Autor': 'Apple 23 Maio 2021',
        'tipo': 'laptop',
        'Descrição': 'Ao longo dos anos, o Windows 10 tem trazido melhorias significativas ao Gestor de Tarefas. '
                     'Este deixou de ser um simples ponto de controlo de processos para ser também uma fonte de '
                     'informação útil e muito importante.'
                     'No meio de todas as alterações, há elementos que acabam por ficar esquecidos. '
                     'O Gestor de Tarefas consegue dar ainda mais informação e observar o Windows 10 como um todo, '
                     'oferecendo o controlo que os utilizadores precisam.'
    }


    noticias = {
        'titulos': [news,news2,news3]
    }

    return render(request, 'website/windows_news.html',context=noticias)

def linux_page_view(request):
    news = {
        'nome':'Chegou o novo Ubuntu 21.04! Impossível não instalar',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2021/04/ubn_00.jpg',
        'Autor':'Linux 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'Abril é o mês do Ubuntu! Tal como prometido pela Canonical, a versão final do Ubuntu 21.04 '
                    'iria ser lançada a 22 deste mês e a expectativa era muito por parte dos '
                    'utilizadores que acompanham e usam esta distribuição.'
    }

    news2 = {
        'nome':'O Linux do Windows 10 já tem disponível a tão esperada interface gráfica',
        'img':'https://pplware.sapo.pt/wp-content/uploads/2019/05/windows-linux-1.jpg',
        'Autor':'Linux 23 Maio 2021',
        'tipo':'laptop',
        'Descrição':'Quando a Microsoft trouxe o Linux para dentro do Windows 10, '
                    'muitos vaticinaram como certo este projeto morrer com o '
                    'tempo. A verdade é que se tem mantido forte e com cada vez mais'
                    'adeptos, mostrando que esta união parece ter vindo para ficar.'
    }

    news3 = {
        'nome': 'Kali Linux 2021.1 já está disponível para download!',
        'img': 'https://pplware.sapo.pt/wp-content/uploads/2020/11/iphone_13_sem_porta01.jpg',
        'Autor': 'Linux 23 Maio 2021',
        'tipo': 'laptop',
        'Descrição': 'Estava à espera da primeira versão de 2021 do Kali Linux? A espera acabou porque a nova versão da '
                     'distribuição direcionada para o hacking ético chegou. Prepare já uma máquina virtual ou a máquina'
                     ' nativa para explorar todas as novidades.'
    }

    news4 = {
        'nome': 'PCLinuxOS 2021.02: A distro Linux para testar em confinamento',
        'img': 'https://pplware.sapo.pt/wp-content/uploads/2021/02/pclinux_00.jpg',
        'Autor': 'Linux 23 Maio 2021',
        'tipo': 'laptop',
        'Descrição': 'O PCLinuxOS é uma distribuição Linux user-friendly, com suporte out-of-the-box para os mais '
                     'diversos dispositivos de hardware e que tem usa como ambiente gráfico principal '
                     'o KDE (também está disponível com o MATE e Xfce).'
    }


    noticias = {
        'titulos': [news,news2,news3,news4]
    }
    return render(request, 'website/linux_news.html',context=noticias)

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
