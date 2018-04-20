# Generated by Django 2.0 on 2018-04-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0004_auto_20180418_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_code',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]