# Generated by Django 2.0 on 2018-03-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0002_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='fcm_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
