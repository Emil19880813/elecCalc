# Generated by Django 2.2.10 on 2020-04-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0009_auto_20200402_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='voltage',
            field=models.DecimalField(choices=[(0, 0.23), (1, 0.4), (2, 15)], decimal_places=2, default=1, max_digits=3),
        ),
    ]
