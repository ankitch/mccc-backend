# Generated by Django 2.0 on 2018-04-03 09:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0011_auto_20180329_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
            options={
                'verbose_name': 'Additional Fields',
            },
        ),
    ]
