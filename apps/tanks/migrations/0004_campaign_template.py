# Generated by Django 2.0 on 2018-03-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0003_customer_fcm_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.TextField(blank=True),
        ),
    ]
