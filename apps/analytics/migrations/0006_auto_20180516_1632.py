# Generated by Django 2.0 on 2018-05-16 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_objectviewed_campaign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectviewed',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='objectviewed',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='objectviewed',
            name='short_url',
        ),
        migrations.DeleteModel(
            name='ObjectViewed',
        ),
    ]
