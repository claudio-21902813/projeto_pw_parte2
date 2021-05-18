from django import forms
from django.forms import ModelForm
from .models import *


class contactForm(ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(),
            'prioridade': forms.TextInput(),
        }

        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'Questao1': forms.TextInput(),
            'p2': forms.TextInput(),
        }
