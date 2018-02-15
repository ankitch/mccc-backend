# Generated by Django 2.0.1 on 2018-02-15 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('tanks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='users.Company'),
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='users.Company'),
        ),
        migrations.AddField(
            model_name='customer',
            name='lists',
            field=models.ManyToManyField(related_name='customer', to='tanks.List'),
        ),
    ]