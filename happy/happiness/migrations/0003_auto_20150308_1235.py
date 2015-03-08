# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happiness', '0002_auto_20141207_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_content',
            new_name='content',
        ),
    ]
