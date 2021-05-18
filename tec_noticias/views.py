from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import *
from .models import Contacto


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

	context = {'form': form}

	return render(request, 'website/contact.html',context)

def quizz_view(request):
	form = QuizzForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('tec_noticias:home'))

	context = {'form': form}

	return render(request, 'website/quizz.html',context)
