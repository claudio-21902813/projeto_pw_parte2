
from django.urls import path

from . import views

app_name = "tec_noticias"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
]