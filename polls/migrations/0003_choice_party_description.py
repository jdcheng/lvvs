# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='party_description',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
