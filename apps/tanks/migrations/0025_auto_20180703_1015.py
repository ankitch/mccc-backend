# Generated by Django 2.0 on 2018-07-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0024_auto_20180702_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='type',
            field=models.CharField(choices=[('Bulk', 'Bulk'), ('Regular', 'Regular')], max_length=50),
        ),
    ]
