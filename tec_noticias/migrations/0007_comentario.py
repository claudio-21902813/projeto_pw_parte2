# Generated by Django 3.2.3 on 2021-05-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tec_noticias', '0006_alter_quizz_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('campo1', models.TextField(max_length=20)),
                ('campo2', models.IntegerField(default=20)),
                ('campo3', models.TextField(max_length=20)),
                ('campo4', models.TextField(max_length=20)),
                ('campo5', models.EmailField(max_length=40)),
                ('campo6', models.BooleanField()),
                ('campo7', models.TextField(max_length=20)),
                ('campo8', models.TextField(max_length=20)),
                ('campo9', models.TextField(max_length=20)),
                ('campo10', models.TextField(max_length=20)),
            ],
        ),
    ]