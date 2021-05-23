
from django.urls import path

from . import views

app_name = "tec_noticias"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('info', views.info_page_view, name='info'),
    path('quizz',views.quizz_view,name='quizz'),
    path('resultado/<int:id>',views.quizz_resultado,name='quizz_resultado'),
    path('contacto', views.contact_page_view, name='contacto'),
    path('contactoEditar/<str:email>', views.edita_contacto, name='edita_contacto'),
    path('contactoElimina/<str:email>', views.apaga_contacto, name='apaga_contacto'),
    path('apple:noticias',views.apple_page_view,name='apple'),
    path('windows:noticias',views.windows_page_view,name='windows'),
    path('linux:noticias',views.linux_page_view,name='linux'),
    path('about', views.about_page_view, name='about'),
    path('comentario',views.comentario_page_view,name='comentario'),
    path('comentario_resultados/<int:id>',views.comentario_resultado,name='comentario_resultado')
]