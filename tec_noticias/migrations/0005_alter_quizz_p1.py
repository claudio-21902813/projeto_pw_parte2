# Generated by Django 3.2.3 on 2021-05-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tec_noticias', '0004_auto_20210519_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='p1',
            field=models.CharField(max_length=10),
        ),
    ]