# Generated by Django 2.0 on 2018-07-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0025_auto_20180703_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
