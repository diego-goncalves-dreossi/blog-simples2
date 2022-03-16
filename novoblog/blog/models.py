from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Artigo(models.Model):
    # Coluna id é criada automaticamente para ser a chave primária
    titulo = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255,unique=True)
    resumo = RichTextField()
    # Strings com tamanho até 255 caracteres.
    #slug = models.SlugField(max_length=255,unique=True)
    # Texto usado na url dos artigos: www.ex.com.br/slug-django (contem letras,numeros,_,ifens). Unique diz que valor não pode se repetir na tabela.
    autor = models.ForeignKey(User,on_delete=models.PROTECT)
    # Chave estrangeira, guarda id do autor do artigo. (Tipo da chave, o que acontece caso usuário seja deletado), nesse caso sendo protegido o artigo
    texto = RichTextUploadingField()
    # Campo sem tamanho máximo.
    data_pub = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    # Salva a data de quando for alterado o artigo.

    # Ordenar por mais novo
    #class Meta:
    #    ordering = ("-data_pub",)

    # Colocar campo de imagem depois

    # Muda a descrição do post no admin
    def __str__(self):
        return self.titulo

    # Define a url de um recurso
    # def get_absolute_url(self):
    #    return reverse("blogapp:detalhe", kwargs={"slug": self.slug})
        #               app: nome da url argumento slug para ser passado      
        # urls.py app_name: name
        # app_name = "blogapp"
        # path("<slug:slug>/",views.ArtigoDetalhe.as_view(),name="detalhe") 