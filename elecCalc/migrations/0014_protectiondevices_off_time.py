# Generated by Django 2.2.10 on 2020-03-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecCalc', '0013_auto_20200324_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='protectiondevices',
            name='off_time',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=2),
        ),
    ]