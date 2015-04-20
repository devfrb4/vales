# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0005_auto_20150420_2230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notas',
            new_name='Notes',
        ),
    ]
