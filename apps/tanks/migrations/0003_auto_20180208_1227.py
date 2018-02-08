# Generated by Django 2.0.1 on 2018-02-08 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0002_auto_20180208_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lists',
            field=models.ManyToManyField(related_name='customers', through='tanks.CustomerList', to='tanks.List'),
        ),
        migrations.AddField(
            model_name='customerlist',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tanks.Customer'),
            preserve_default=False,
        ),
    ]
