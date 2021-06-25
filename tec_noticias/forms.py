from django import forms
from django.forms import ModelForm
from .models import *


class contactForm(ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class comentarioNoticiaForm(ModelForm):
    class Meta:
        model = Comentario_Noticia
        fields = ('autor','texto','data')

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        # texto a exibir junto à janela de inserção
        labels = {
            'p1': 'Considera que a apple tem tendencia a ter melhores noticias por ser uma marca de "luxo"?',
            'p2': 'Sabe quais sao os autores do website?',
            'p3': 'Em que data começou PW?',
            'p4': 'E a hora?',
            'p5': 'pi / 2? - com 2 casas decimais',
            'p6': 'Comente o quiz ate agora ( este nao conta !)',
            'p7': 'O Website e de noticias ou de anuncios?',
            'p8': 'Foi Baseado no sapo.pt?',
            'p9': 'Gosta das aulas de PW??',
            'p10': 'Programação ou Gestão de Projetos??',
        }

        widgets = {
            'p1': forms.TextInput(attrs={'placeholder': ''}),
            'p3': forms.DateTimeInput(attrs={'placeholder': 'yyyy:mm:dd'}),
            'p4': forms.TimeInput(attrs={'placeholder': 'hh:mm'}),
        }

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

        labels = {
            'campo1': 'Nome',
            'campo2': 'Idade',
            'campo3': 'O website é visualmente atrativo?',
            'campo4':"Cumpre boas praticas de UI/UX?",
            'campo5':'Email?',
            'campo6':'A tablete de Cores condiz',
            'campo7':'O website cumpre as 10 normas de Nielsen?',
            'campo8':'Encontrou algum Bug Grafico ou funcional?',
            'campo9': 'O website tem muitos erros ortográficos?',
            'campo10':'Construtivamente, Aponte o que achou de errado e sugestões de melhoria'
        }




