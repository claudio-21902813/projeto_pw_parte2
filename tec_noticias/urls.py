
from django.urls import path

from . import views

app_name = "tec_noticias"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('info', views.info_page_view, name='info'),
    path('quizz',views.quizz_view,name='quizz'),
    path('contacto', views.contact_page_view, name='contacto'),
    path('apple:noticias',views.apple_page_view,name='apple'),
    path('windows:noticias',views.windows_page_view,name='windows'),
    path('linux:noticias',views.linux_page_view,name='linux'),
]