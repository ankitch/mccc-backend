# Generated by Django 2.0 on 2018-07-02 09:42

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0022_auto_20180618_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='to_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='campaign',
            name='type',
            field=models.CharField(choices=[('Bulk', 'Bulk'), ('Regular', 'Regular')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='tanks.List'),
        ),
    ]
