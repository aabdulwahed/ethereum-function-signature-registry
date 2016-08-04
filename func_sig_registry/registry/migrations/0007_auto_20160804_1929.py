# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0006_remove_bytessignature_unicode_bytes4_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='bytes_signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registry.BytesSignature'),
        ),
    ]