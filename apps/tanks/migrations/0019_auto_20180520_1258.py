# Generated by Django 2.0 on 2018-05-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0018_auto_20180513_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
