
from django.urls import path

from . import views

app_name = "tec_noticias"

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='index'),
    path("sections/<str:num>", views.section, name="section"),
    path("criarComentario",views.comentario_page_view,name="comentario"),
    path('quizz', views.quizz_view, name='quizz'),
    path('guardaContacto', views.guarda_contacto, name='guardaContacto'),
    path('contactoEditar/<str:email>', views.edita_contacto, name='edita_contacto'),
    path('contactoElimina/<str:email>', views.apaga_contacto, name='apaga_contacto'),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('getNews',views.Get_Noticias,name="getNews"),
]