# Generated by Django 2.0 on 2018-06-18 09:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0026_campaign_email_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingconfig',
            name='attributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'age': '', 'sex': ''}, null=True),
        ),
    ]
