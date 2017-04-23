# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0009_invoices_invoice_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='invoice_identifier',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='telephone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]