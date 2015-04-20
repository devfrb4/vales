# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0004_auto_20150420_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='color',
            field=models.CharField(verbose_name='Color', max_length=25),
        ),
        migrations.AlterField(
            model_name='notas',
            name='content',
            field=models.TextField(verbose_name='contenido', max_length=300),
        ),
        migrations.AlterField(
            model_name='notas',
            name='title',
            field=models.CharField(verbose_name='Titulo', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
