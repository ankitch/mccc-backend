# Generated by Django 2.0 on 2018-08-01 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replies',
            old_name='company_id',
            new_name='company',
        ),
    ]
