# Generated by Django 2.0 on 2018-03-29 07:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0010_auto_20180329_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segments',
            name='query',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
