# Generated by Django 4.1 on 2022-10-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_pagina_autor_alter_pagina_fechapublicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenpagina',
            name='fechaPublicacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]