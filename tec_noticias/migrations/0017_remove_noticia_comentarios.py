# Generated by Django 3.2.3 on 2021-05-25 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tec_noticias', '0016_auto_20210525_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='comentarios',
        ),
    ]