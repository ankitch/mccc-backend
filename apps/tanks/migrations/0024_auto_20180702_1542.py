# Generated by Django 2.0 on 2018-07-02 09:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0023_auto_20180702_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='to_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), blank=True, null=True, size=None),
        ),
    ]
