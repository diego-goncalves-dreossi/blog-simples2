from django.urls import path
from . import views

# Define nome do app usado depois
app_name = "blog"
# Caminhos url do app
urlpatterns = [
    path("",views.paginaInicial,name="home"),
    path('artigos/<int:artigo_id>',views.verArtigo, name="artigo")
]