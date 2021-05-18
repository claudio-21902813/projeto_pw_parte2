from django.db import models

# Create your models here.
class Contacto(models.Model):
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=40)


    def __str__(self):
        return self.nome


class Quizz(models.Model):
    p1 = models.CharField(max_length=40)
    p2 = models.CharField(max_length=10)
    p3 = models.CharField(max_length=40)
    p4 = models.CharField(max_length=40)
    p5 = models.CharField(max_length=40)
    p6 = models.CharField(max_length=40)
    p7 = models.CharField(max_length=40)
    p8 = models.CharField(max_length=40)
    p9 = models.CharField(max_length=40)
    p10 = models.CharField(max_length=40)

