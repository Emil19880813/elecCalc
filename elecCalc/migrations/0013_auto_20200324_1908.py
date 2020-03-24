# Generated by Django 2.2.10 on 2020-03-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0012_auto_20200324_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='cable',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cable',
            name='core',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cable',
            name='layer_factor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
        migrations.AddField(
            model_name='cable',
            name='length',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='cable',
            name='overload_factor',
            field=models.DecimalField(choices=[(0, 1.2), (1, 1.45), (2, 1.6), (3, 1.9)], decimal_places=2, default=0, max_digits=3),
        ),
    ]