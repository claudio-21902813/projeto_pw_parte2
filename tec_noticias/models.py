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

