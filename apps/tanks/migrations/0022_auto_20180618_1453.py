# Generated by Django 2.0 on 2018-06-18 09:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0021_auto_20180613_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingconfig',
            name='attributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'age': '', 'sex': ''}, null=True),
        ),
    ]
