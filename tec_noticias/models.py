from django.db import models

# Create your models here.
class Contacto(models.Model):
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=40)


    def __str__(self):
        return self.nome


class Quizz(models.Model):
    id = models.AutoField(primary_key=True)
    p1 = models.CharField(max_length=10)
    p2 = models.BooleanField()
    p3 = models.DateField()
    p4 = models.TimeField()
    p5 = models.FloatField()
    p6 = models.TextField()
    p7 = models.CharField(max_length=40)
    p8 = models.CharField(max_length=40)
    p9 = models.CharField(max_length=40)
    p10 = models.CharField(max_length=40)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    campo1 = models.CharField(max_length=20)
    campo2 = models.IntegerField(default=20)
    campo3 = models.CharField(max_length=20)
    campo4 = models.CharField(max_length=20)
    campo5 = models.EmailField(max_length=40)
    campo6 = models.BooleanField()
    campo7 = models.CharField(max_length=20)
    campo8 = models.CharField(max_length=20)
    campo9 = models.CharField(max_length=20)
    campo10 = models.TextField(max_length=20)

    def __str__(self):
        return "Nome: " + self.campo1 +  " Idade: " + str(self.campo2) + " Email: " + self.campo5


class Categoria(models.Model):
    tipo = models.CharField(max_length=10)
    icon = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo

class Noticia(models.Model):
    titulo = models.CharField(max_length=90)
    sinopse = models.CharField(max_length=500)
    imagem = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="categoria")
    descricao = models.TextField(max_length=1000)

