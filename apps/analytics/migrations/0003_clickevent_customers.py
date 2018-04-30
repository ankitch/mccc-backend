# Generated by Django 2.0 on 2018-04-27 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0013_delete_settings'),
        ('analytics', '0002_auto_20180420_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='clickevent',
            name='customers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tanks.Customer'),
        ),
    ]