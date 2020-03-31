# Generated by Django 2.2.10 on 2020-03-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0002_protectiondevices_kr_factor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cable',
            name='overload_factor',
        ),
        migrations.AddField(
            model_name='protectiondevices',
            name='k2_factor',
            field=models.DecimalField(choices=[(0, 1.2), (1, 1.45), (2, 1.6), (3, 1.9)], decimal_places=2, default=0, max_digits=3),
        ),
    ]
